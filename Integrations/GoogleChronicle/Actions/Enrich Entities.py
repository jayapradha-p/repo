from __future__ import annotations

import re
from typing import Any, TYPE_CHECKING

from datetime import datetime, timedelta
from urllib.parse import urlparse, ParseResult

from SiemplifyDataModel import EntityTypes, DomainEntityInfo
from TIPCommon.base.action.base_enrich_action import EnrichAction
from TIPCommon.base.action.data_models import EntityTypesEnum
from TIPCommon.extraction import extract_action_param, extract_configuration_param
from TIPCommon.transformation import dict_to_flat

import consts
from exceptions import (
    GoogleChronicleValidationError,
    GoogleChronicleParameterValidationError,
)
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2
from utils import (
    get_iso_time_range,
    parse_iso_time,
    restructure_entity_details,
    validate_api_root_for_backstory,
)


if TYPE_CHECKING:
    from datamodels import (
        EntitySummary,
        DetailedEntitySummary,
        RelatedEntitiesResponse,
    )
    from TIPCommon.types import SingleJson


def build_enrichment_payload(enriched_data: SingleJson) -> SingleJson:
    """Builds a complete enrichment payload from various data points.

    This function aggregates details, counts, and metrics into a single
    dictionary for entity enrichment.

    Args:
        enriched_data (SingleJson): The raw data containing all enrichment information.

    Returns:
        A dictionary representing the complete enrichment payload.
    """
    payload: SingleJson = {}
    add_entity_details_to_payload(payload, enriched_data)
    add_related_entities_count_to_payload(payload, enriched_data)
    add_metric_data_to_payload(payload, enriched_data)
    add_alert_counts_to_payload(payload, enriched_data)

    return payload


def add_entity_details_to_payload(
    payload: SingleJson,
    enriched_data: SingleJson,
) -> None:
    """Adds flattened entity details to the enrichment payload.

    Args:
        payload (SingleJson): The enrichment payload to update.
        enriched_data (SingleJson): The data containing entity details.
    """
    entity_details: Any = enriched_data.get("entity", {})
    if isinstance(entity_details, dict):
        payload.update(dict_to_flat(entity_details))


def add_related_entities_count_to_payload(
    payload: SingleJson,
    enriched_data: SingleJson,
) -> None:
    """Adds the count of related entities to the enrichment payload.

    Args:
        payload (SingleJson): The enrichment payload to update.
        enriched_data (SingleJson): The data containing the list of related entities.
    """
    if consts.RELATED_ENTITIES_KEY in enriched_data:
        payload["related_entities_count"] = len(
            enriched_data[consts.RELATED_ENTITIES_KEY]
        )


def add_metric_data_to_payload(
    payload: SingleJson,
    enriched_data: SingleJson,
) -> None:
    """Adds first and last seen timestamps to the enrichment payload.

    Args:
        payload (SingleJson): The enrichment payload to update.
        enriched_data (SingleJson): The data containing metric information.
    """
    metric: Any = enriched_data.get("metric", {})
    if isinstance(metric, dict):
        if consts.FIRST_SEEN_KEY in metric:
            payload[consts.ENRICHMENT_FIRST_SEEN_KEY] = metric[consts.FIRST_SEEN_KEY]
        if consts.LAST_SEEN_KEY in metric:
            payload[consts.ENRICHMENT_LAST_SEEN_KEY] = metric[consts.LAST_SEEN_KEY]


def add_alert_counts_to_payload(
    payload: SingleJson,
    enriched_data: SingleJson,
) -> None:
    """Adds alert counts per rule to the enrichment payload.

    Args:
        payload (SingleJson): The enrichment payload to update.
        enriched_data (SingleJson): The data containing alert count information.
    """
    alert_counts: Any = enriched_data.get("alertCounts", [])
    if isinstance(alert_counts, list):
        for item in alert_counts:
            rule_name: Any = item.get("rule")
            count: Any = item.get("count")
            if rule_name and count is not None:
                clean_rule_name: str = consts.INVALID_KEY_CHARACTERS_REGEX.sub(
                    "",
                    rule_name,
                )
                payload[f"alert_count_{clean_rule_name}"] = count


class EnrichEntities(EnrichAction):

    def __init__(self) -> None:
        super().__init__(consts.ENRICH_ENTITIES_SCRIPT_NAME)
        self.api_time_start: str = ""
        self.api_time_end: str = ""

    def _extract_action_parameters(self) -> None:
        self.params.user_service_account = extract_configuration_param(
            self.soar_action,
            provider_name=consts.INTEGRATION_NAME,
            param_name="User's Service Account",
            remove_whitespaces=False,
        )
        self.params.workload_identity_email = extract_configuration_param(
            self.soar_action,
            provider_name=consts.INTEGRATION_NAME,
            param_name="Workload Identity Email",
        )
        self.params.api_root = extract_configuration_param(
            self.soar_action,
            provider_name=consts.INTEGRATION_NAME,
            param_name="API Root",
            is_mandatory=True,
            print_value=True,
        )
        self.params.verify_ssl = extract_configuration_param(
            self.soar_action,
            provider_name=consts.INTEGRATION_NAME,
            param_name="Verify SSL",
            is_mandatory=True,
            input_type=bool,
            print_value=True,
        )
        self.params.namespace = extract_action_param(
            self.soar_action,
            param_name="Namespace",
            print_value=True,
        )
        self.params.time_frame = extract_action_param(
            self.soar_action,
            param_name="Time Frame",
            print_value=True,
            default_value="Last Month",
        )
        self.params.start_time = extract_action_param(
            self.soar_action,
            param_name="Start Time",
            print_value=True,
        )
        self.params.end_time = extract_action_param(
            self.soar_action,
            param_name="End Time",
            print_value=True,
        )

    def _validate_params(self) -> None:
        if (
            self.params.start_time or self.params.end_time
        ) and self.params.time_frame != "Custom":
            raise GoogleChronicleParameterValidationError(
                "Start Time or End Time can only be provided when 'Custom' is "
                "selected for the Time Frame parameter."
            )

        if self.params.start_time and self.params.end_time:
            start_dt: datetime = parse_iso_time(self.params.start_time)
            end_dt: datetime = parse_iso_time(self.params.end_time)

            if max(start_dt, end_dt) == start_dt and start_dt != end_dt:
                raise GoogleChronicleParameterValidationError(
                    "The interval Start Time has to be before the End Time."
                )

        validate_api_root_for_backstory(self.params.api_root)
        self.api_time_start, self.api_time_end = get_iso_time_range(
            self.params.time_frame, self.params.start_time, self.params.end_time
        )

    def _init_api_clients(self) -> GoogleChronicleManagerV2:
        return GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=self.params.user_service_account,
            chronicle_soar=self.soar_action,
            api_root=self.params.api_root,
            verify_ssl=self.params.verify_ssl,
            workload_identity_email=self.params.workload_identity_email,
        )

    def _perform_enrich_action(
        self,
        current_entity: DomainEntityInfo,
    ) -> None:
        if not current_entity:
            return

        enriched_data: SingleJson | None = self._get_enriched_data_for_entity(
            current_entity
        )

        if not enriched_data:
            raise GoogleChronicleValidationError(
                f"No enrichment data found for {current_entity.identifier}"
            )
        if enriched_data:
            self.entity_results = enriched_data

        payload: SingleJson = build_enrichment_payload(enriched_data)
        if payload:
            self.enrichment_data = {
                f"{consts.ENRICHMENT_PREFIX}{field_name}": field_value
                for field_name, field_value in payload.items()
            }

    def _get_entity_types(self) -> list[EntityTypesEnum]:
        supported_type_values: list[str] = [
            enum.value.lower() for enum in consts.SUPPORTED_TYPE_VALUES
        ]

        if not any(
            entity.entity_type.lower() in supported_type_values
            for entity in self.soar_action.target_entities
        ):
            raise GoogleChronicleValidationError(
                "Action failed because no supported entities (IP, Hostname, Domain, URL"
                ", Hash, User, MAC) were found in the action's scope. Please ensure the"
                " action is running on at least one supported entity."
            )

        return consts.SUPPORTED_TYPE_VALUES

    def _get_enriched_data_for_entity(
        self,
        entity: DomainEntityInfo,
    ) -> SingleJson | None:
        query: str | None = self._get_query_for_entity(entity)
        if not query:
            return None

        selected_summary: EntitySummary | None = self._find_best_entity_summary(
            entity, query
        )
        if not selected_summary:
            return None

        full_details: SingleJson | None = self._get_full_enrichment_details(
            selected_summary
        )
        if not full_details:
            return None

        return self._format_json_result(full_details)

    def _get_query_for_entity(self, entity: DomainEntityInfo) -> str | None:
        entity_value: str | None = self._get_entity_value_for_query(entity)
        if not entity_value:
            return None

        query_template: str | None = self._get_template_for_entity(entity)
        if not query_template:
            self.soar_action.LOGGER.info(
                f"Unsupported entity type: {entity.entity_type}. "
                f"Skipping {entity.identifier}."
            )
            return None

        query: str = query_template.format(value=entity_value)
        self.soar_action.LOGGER.info(
            f"Constructed query for {entity.identifier}: {query}"
        )
        return query

    def _get_entity_value_for_query(self, entity: DomainEntityInfo) -> str | None:
        entity_value: str = entity.identifier.lower()

        if entity.entity_type == EntityTypes.URL:
            parsed_url: ParseResult = urlparse(entity_value)
            domain: str = parsed_url.netloc or parsed_url.path.split("/")[0]
            if not domain:
                self.soar_action.LOGGER.warn(
                    f"Could not extract domain from URL: {entity.identifier}."
                )
                return None
            return domain

        return entity_value

    def _get_template_for_entity(self, entity: DomainEntityInfo) -> str | None:
        entity_type: int = entity.entity_type
        entity_type_key: str = str(entity_type).lower()

        if entity_type == EntityTypes.USER:
            is_email: re.Match[str] | None = consts.EMAIL_REGEX.match(entity.identifier)
            template_key: str = (
                consts.USER_EMAIL_QUERY_KEY
                if is_email
                else consts.USER_GENERIC_QUERY_KEY
            )
            return consts.ENTITY_QUERY_TEMPLATES.get(template_key)

        return consts.ENTITY_QUERY_TEMPLATES.get(entity_type_key)

    def _get_one_hour_time_range_iso(self) -> tuple[str, str]:
        now: datetime = datetime.utcnow()
        one_hour_ago: datetime = now - timedelta(hours=1)
        now_iso: str = now.isoformat(timespec="milliseconds") + "Z"
        one_hour_ago_iso: str = one_hour_ago.isoformat(timespec="milliseconds") + "Z"
        return one_hour_ago_iso, now_iso

    def _query_for_entity_summaries(self, query: str) -> list[EntitySummary]:
        start_time: str
        end_time: str
        start_time, end_time = self._get_one_hour_time_range_iso()
        self.soar_action.LOGGER.info(
            f"Querying for entity summaries with query: {query}"
        )
        return self.api_client.summarize_entities_from_query(
            query=query,
            start_time=start_time,
            end_time=end_time,
        )

    def _find_best_entity_summary(
        self,
        entity: DomainEntityInfo,
        query: str,
    ) -> EntitySummary | None:
        self.soar_action.LOGGER.info(
            f"Querying for summaries for entity: {entity.identifier}"
        )
        found_summaries: list[EntitySummary] = self._query_for_entity_summaries(query)

        namespace_to_filter: str | None = (
            self.params.namespace
            if entity.entity_type in consts.NAMESPACE_FILTER_ENTITY_TYPES
            else None
        )
        selected_summary: EntitySummary | None = self._select_entity_summary(
            found_summaries, namespace_to_filter
        )

        if not selected_summary:
            return None

        return selected_summary

    def _get_detailed_summary(
        self,
        entity_summary: EntitySummary,
    ) -> SingleJson | None:
        self.soar_action.LOGGER.info(
            f"Fetching detailed summary for entity ID: {entity_summary.name}."
        )
        detailed_summary: DetailedEntitySummary | None = (
            self.api_client.summarize_entity(
                entity_id=entity_summary.name,
                start_time=self.api_time_start,
                end_time=self.api_time_end,
                initial_summary_info=entity_summary.raw_data,
            )
        )
        if not detailed_summary:
            self.soar_action.LOGGER.info(
                f"No detailed information found for entity ID {entity_summary.name}."
            )
            return None
        return detailed_summary.to_json()

    def _get_related_entities(self, entity_id: str) -> list | None:
        self.soar_action.LOGGER.info(
            f"Fetching related entities for entity ID: {entity_id}."
        )
        related_entities: RelatedEntitiesResponse | None = (
            self.api_client.find_related_entities(
                entity_id=entity_id,
                start_time=self.api_time_start,
                end_time=self.api_time_end,
            )
        )
        if related_entities and related_entities.related_entities:
            return related_entities.related_entities
        return None

    def _get_full_enrichment_details(
        self,
        selected_summary: EntitySummary,
    ) -> SingleJson | None:
        self.soar_action.LOGGER.info(
            f"Selected entity ID: {selected_summary.name}. Fetching full details."
        )

        detailed_summary: SingleJson | None = self._get_detailed_summary(
            selected_summary
        )
        if not detailed_summary:
            return None

        final_result: SingleJson = restructure_entity_details(detailed_summary)

        self._fetch_and_add_related_entities(final_result, selected_summary.name)

        return final_result

    def _fetch_and_add_related_entities(
        self,
        result_data: SingleJson,
        entity_id: str,
    ) -> None:
        related_entities: list | None = self._get_related_entities(entity_id)
        if related_entities:
            result_data[consts.RELATED_ENTITIES_KEY] = related_entities

    def _format_json_result(
        self,
        raw_result: SingleJson,
    ) -> SingleJson | None:
        if not any(raw_result.get(key) for key in consts.ENRICHMENT_KEYS):
            self.soar_action.LOGGER.info(
                "Entity found, but no meaningful information available."
            )
            return None

        return self._reorder_dict_keys(raw_result, consts.ENRICHED_ORDERED_KEYS)

    def _reorder_dict_keys(
        self,
        data: SingleJson,
        ordered_keys: list[str],
    ) -> SingleJson:
        reordered_result: SingleJson = {
            key: data[key] for key in ordered_keys if key in data
        }
        reordered_result.update(
            {key: value for key, value in data.items() if key not in reordered_result}
        )
        return reordered_result

    def _find_summary_by_specific_namespace(
        self,
        summaries: list[EntitySummary],
        namespace: str,
    ) -> EntitySummary | None:
        summary: EntitySummary
        for summary in summaries:
            if summary.namespace == namespace:
                self.soar_action.LOGGER.info(
                    "Found and selected entity with user-provided namespace: "
                    f"'{namespace}'."
                )
                return summary
        self.soar_action.LOGGER.info(
            f"A namespace '{namespace}' was provided, but no matching entity was found."
        )

        return None

    def _find_first_summary_with_any_namespace(
        self,
        summaries: list[EntitySummary],
    ) -> EntitySummary | None:
        summary_with_namespace: EntitySummary | None = next(
            (s for s in summaries if s.namespace), None
        )
        if summary_with_namespace:
            self.soar_action.LOGGER.info(
                "No user namespace provided. Selected the first entity found that has a"
                " namespace."
            )
        return summary_with_namespace

    def _select_entity_summary(
        self,
        found_summaries: list[EntitySummary],
        user_namespace: str | None,
    ) -> EntitySummary | None:
        if not found_summaries:
            return None

        if user_namespace:
            return self._find_summary_by_specific_namespace(
                found_summaries, user_namespace
            )

        summary_with_any_namespace: EntitySummary | None = (
            self._find_first_summary_with_any_namespace(found_summaries)
        )
        if summary_with_any_namespace:
            return summary_with_any_namespace

        self.soar_action.LOGGER.info(
            "No entities with a namespace were found. Selecting the first "
            "available entity from the results."
        )
        return found_summaries[0]

    def _is_unwanted_result(self, result: Any) -> bool:
        return isinstance(result, dict) and "execution_status" in result

    def _get_adjusted_json_results(self) -> SingleJson:
        if isinstance(self._json_results, dict):
            self._json_results = {
                identifier: result
                for identifier, result in self._json_results.items()
                if not self._is_unwanted_result(result)
            }

        return super()._get_adjusted_json_results()

    def _finalize_action_on_success(self) -> None:
        successful_ids: list[str] = sorted(
            e.identifier for e in self.entities_to_update
        )

        all_target_entity_ids: set[str] = {
            entity.identifier for entity in self.soar_action.target_entities
        }
        failed_ids: list[str] = sorted(all_target_entity_ids - set(successful_ids))

        self.result_value = bool(successful_ids)

        if successful_ids:
            self.output_message = (
                "Successfully enriched the following entities using "
                f"information from Google SecOps: {', '.join(successful_ids)}."
            )
            if failed_ids:
                failed_msg: str = (
                    "Action wasn't able to enrich the following entities "
                    "using information from Google SecOps: "
                    f"{', '.join(failed_ids)}."
                )
                self.output_message += f"\n{failed_msg}"
        else:
            self.output_message = (
                "None of the provided entities were enriched using information from "
                "Google SecOps."
            )


def main() -> None:
    action = EnrichEntities()
    action.run()


if __name__ == "__main__":
    main()
