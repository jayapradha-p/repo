from SiemplifyAction import SiemplifyAction
from ScriptResult import (
    EXECUTION_STATE_COMPLETED,
    EXECUTION_STATE_FAILED,
    EXECUTION_STATE_TIMEDOUT,
)
from SiemplifyDataModel import EntityTypes
from SiemplifyUtils import (
    convert_dict_to_json_result_dict,
    convert_unixtime_to_datetime,
    output_handler,
    unix_now,
)

from TIPCommon.extraction import extract_action_param, extract_configuration_param
from TIPCommon.transformation import construct_csv

import consts
import utils
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2


SCRIPT_NAME = "Enrich Domain"
ENRICHMENT_PREFIX = "G_Chronicle"
SUPPORTED_ENTITIES = [EntityTypes.URL, EntityTypes.HOSTNAME]


@output_handler
def main():
    siemplify = SiemplifyAction()
    siemplify.script_name = f"{consts.INTEGRATION_NAME} - {SCRIPT_NAME}"
    siemplify.LOGGER.info("================= Main - Param Init =================")

    # INIT INTEGRATION CONFIGURATION:
    creds = extract_configuration_param(
        siemplify,
        provider_name=consts.INTEGRATION_NAME,
        param_name="User's Service Account",
        remove_whitespaces=False,
    )
    workload_identity_email = extract_configuration_param(
        siemplify,
        provider_name=consts.INTEGRATION_NAME,
        param_name="Workload Identity Email",
    )
    api_root = extract_configuration_param(
        siemplify,
        provider_name=consts.INTEGRATION_NAME,
        param_name="API Root",
        is_mandatory=True,
        print_value=True,
    )
    verify_ssl = extract_configuration_param(
        siemplify,
        provider_name=consts.INTEGRATION_NAME,
        param_name="Verify SSL",
        is_mandatory=True,
        input_type=bool,
        print_value=True,
    )

    lowest_suspicious_severity = extract_action_param(
        siemplify,
        param_name="Lowest Suspicious Severity",
        is_mandatory=True,
        print_value=True,
    )
    mark_na_suspicious = extract_action_param(
        siemplify,
        param_name="Mark Suspicious N/A Severity",
        is_mandatory=False,
        print_value=True,
        default_value=False,
        input_type=bool,
    )
    create_insight = extract_action_param(
        siemplify,
        param_name="Create Insight",
        is_mandatory=False,
        print_value=True,
        default_value=True,
        input_type=bool,
    )
    only_suspicious_insight = extract_action_param(
        siemplify,
        param_name="Only Suspicious Insight",
        is_mandatory=False,
        print_value=True,
        default_value=True,
        input_type=bool,
    )

    lowest_suspicious_severity = consts.IOC_SEVERITIES.get(
        lowest_suspicious_severity.lower()
    )

    siemplify.LOGGER.info("----------------- Main - Started -----------------")

    status = EXECUTION_STATE_COMPLETED
    successful_entities = []
    json_results = {}
    failed_entities = []
    output_message = ""
    result_value = "false"

    try:
        manager = GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=creds,
            chronicle_soar=siemplify,
            api_root=api_root,
            verify_ssl=verify_ssl,
            workload_identity_email=workload_identity_email,
        )
        manager.test_connectivity()

        for entity in siemplify.target_entities:
            is_suspicious = False
            if unix_now() >= siemplify.execution_deadline_unix_time_ms:
                siemplify.LOGGER.error(
                    "Timed out. execution deadline "
                    f"({convert_unixtime_to_datetime(siemplify.execution_deadline_unix_time_ms)}) "
                    "has passed."
                )
                status = EXECUTION_STATE_TIMEDOUT
                break

            try:
                if entity.entity_type not in SUPPORTED_ENTITIES:
                    siemplify.LOGGER.info(
                        f"Entity {entity.identifier} is of unsupported type. "
                        "Skipping."
                    )
                    continue

                siemplify.LOGGER.info(f"Started processing entity: {entity.identifier}")

                domain = (
                    utils.get_domain_from_entity(
                        utils.get_entity_original_identifier(entity)
                    )
                    if entity.entity_type == EntityTypes.URL
                    else utils.get_entity_original_identifier(entity)
                )
                siemplify.LOGGER.info(f"Fetching information for domain {domain}")
                ioc_details = manager.get_ioc_details(domain=domain)
                if ioc_details is None:
                    siemplify.LOGGER.info(
                        f"No information found about {entity.identifier}."
                    )
                    failed_entities.append(entity)
                    continue

                siemplify.LOGGER.info(
                    f"Found information about {domain}. "
                    "Highest source severity: "
                    f"{ioc_details.highest_source_severity[0]}"
                )

                entity.additional_properties.update(
                    ioc_details.as_enrichment(prefix=ENRICHMENT_PREFIX, for_domain=True)
                )
                entity.is_enriched = True

                json_results[entity.identifier] = ioc_details.to_json()

                if (
                    ioc_details.highest_source_severity[1] >= lowest_suspicious_severity
                    or ioc_details.highest_source_severity[1] == 0
                    and mark_na_suspicious
                ):
                    # If at least one of the sources of the IOC have severity gte then lowest_suspicious_severity
                    # or if all have n/a severity and mark_na_suspicious - mark the entity as suspicious
                    siemplify.LOGGER.info("Marking entity as suspicious.")
                    entity.is_suspicious = True
                    is_suspicious = True

                if create_insight and not only_suspicious_insight:
                    siemplify.add_entity_insight(
                        entity, ioc_details.to_insight(for_domain=True)
                    )
                elif create_insight and only_suspicious_insight and is_suspicious:
                    siemplify.add_entity_insight(
                        entity, ioc_details.to_insight(for_domain=True)
                    )

                siemplify.result.add_entity_table(
                    entity.identifier,
                    construct_csv(ioc_details.to_table(for_domain=True)),
                )
                siemplify.result.add_entity_link(
                    entity.identifier, ioc_details.uri[0] if ioc_details.uri else ""
                )

                successful_entities.append(entity)
                siemplify.LOGGER.info(f"Finished processing entity {entity.identifier}")
                ioc_data_found = "false"
                if ioc_details.is_full_data:
                    ioc_data_found = "true"
                json_results[entity.identifier].update({
                    "ioc_data_found": ioc_data_found
                })

            except Exception as e:
                failed_entities.append(entity)
                siemplify.LOGGER.error(
                    f"An error occurred on entity {entity.identifier}"
                )
                siemplify.LOGGER.exception(e)

        if successful_entities:
            output_message += (
                "Successfully enriched the following domains from Google"
                " Chronicle:\n   {}".format(
                    "\n   ".join([entity.identifier for entity in successful_entities])
                )
            )
            siemplify.update_entities(successful_entities)
            result_value = "true"

        else:
            output_message += "No entities were enriched."

        if failed_entities:
            output_message += (
                "\n\nAction was not able to enrich the following URLs from"
                " Google Chronicle:\n   {}".format(
                    "\n   ".join([entity.identifier for entity in failed_entities])
                )
            )

    except Exception as e:
        siemplify.LOGGER.error(f'Error executing action "{SCRIPT_NAME}". Reason: {e}')
        siemplify.LOGGER.exception(e)
        status = EXECUTION_STATE_FAILED
        result_value = "false"
        output_message = f'Error executing action "{SCRIPT_NAME}". Reason: {e}'

    siemplify.result.add_result_json(convert_dict_to_json_result_dict(json_results))
    siemplify.LOGGER.info("----------------- Main - Finished -----------------")
    siemplify.LOGGER.info(f"Status: {status}")
    siemplify.LOGGER.info(f"Result Value: {result_value}")
    siemplify.LOGGER.info(f"Output Message: {output_message}")
    siemplify.end(output_message, result_value, status)


if __name__ == "__main__":
    main()
