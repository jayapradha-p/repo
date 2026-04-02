from copy import deepcopy

from http.client import HTTPResponse, HTTPConnection
from io import BytesIO
from itertools import islice
from typing import Iterator, Dict, Any
import requests
from TIPCommon.types import SingleJson

from consts import MB_IN_BYTES
from datamodels import (
    ActionDetails,
    AddedDataTableRow,
    Alert,
    AlertMetadata,
    Asset,
    CaseData,
    CaseMetadata,
    ChronicleAlert,
    ChronicleCase,
    CuratedRule,
    DataTableDetails,
    DataTableInfo,
    Detection,
    DetailedEntitySummary,
    EntitySummary,
    Event,
    GeminiResponse,
    IOC,
    IOCDetail,
    MultipartResponsePart,
    NewAlertSyncResult,
    Outcomes,
    RawLog,
    RefDataObject,
    ReferenceList,
    RelatedEntitiesResponse,
    RetrohuntObject,
    Rule,
    SiemAlert,
    SiemEvent,
    UdmQueryEvent,
    WatchlistEntity,
)
from utils import normalize_stats_results, seek_to_start


class GoogleChronicleParser:
    """
    Google Chronicle Transformation Layer.
    """

    @staticmethod
    def build_siemplify_ioc_obj(ioc_data, fallback_severity=None):
        raw_data = deepcopy(ioc_data)
        sources = [
            (
                GoogleChronicleParser.build_siemplify_ioc_source_obj({"source": source})
                if isinstance(source, str) else
                GoogleChronicleParser.build_siemplify_ioc_source_obj(source)
            )
            for source in ioc_data.pop("sources", [])
        ]

        return IOC(
            raw_data=raw_data,
            domain_name=(
                raw_data.get("artifact", {}).get("domainName")
                or raw_data.get("artifactIndicator", {}).get("domain")
            ),
            sources=sources,
            fallback_severity=fallback_severity,
            **ioc_data,
        )

    @staticmethod
    def build_siemplify_ioc_source_obj(source_data):
        return IOC.Source(
            raw_data=source_data,
            intRawConfidenceScore=source_data.get("confidenceScore", {}).get(
                "intRawConfidenceScore"
            ),
            normalizedConfidenceScore=source_data.get("confidenceScore", {}).get(
                "normalizedConfidenceScore"
            ),
            **source_data,
        )

    @staticmethod
    def build_siemplify_ioc_sources_list(ioc_detail_data) -> list[IOCDetail.Source]:
        return [
            GoogleChronicleParser.build_siemplify_ioc_detail_source_obj(source)
            for source in ioc_detail_data["sources"]
        ]

    @staticmethod
    def build_siemplify_ioc_feeds_list(ioc_detail_data) -> list[IOCDetail.Source]:
        return [
            GoogleChronicleParser.build_siemplify_ioc_detail_source_obj(
                {
                    **feed["metadata"],
                    **ioc_data
                }
            )
            for feed in ioc_detail_data.get("feeds", [])
            for ioc_data in feed.get("iocs", [])
        ]

    @staticmethod
    def build_siemplify_ioc_detail_obj(ioc_detail_data) -> IOCDetail:
        """Build an instance of IOCDetail from parsed JSON response."""
        raw_data = deepcopy(ioc_detail_data)
        sources = (
            GoogleChronicleParser.build_siemplify_ioc_sources_list(ioc_detail_data)
            if "sources" in ioc_detail_data else
            GoogleChronicleParser.build_siemplify_ioc_feeds_list(ioc_detail_data)
        )
        return IOCDetail(
            raw_data=raw_data,
            sources=sources,
            uri=ioc_detail_data.get("uri")
        )

    @staticmethod
    def build_siemplify_ioc_detail_source_obj(source_data):
        raw_data = deepcopy(source_data)
        addresses = (
            GoogleChronicleParser.build_siemplify_ioc_detail_source_addresses_obj(
                source_data.pop("addresses", [])
            ) if "addresses" in source_data else
            GoogleChronicleParser.build_siemplify_ioc_detail_source_addresses_obj([
                el for el in (
                    source_data.get("domainAndPorts"),
                    source_data.get("ipAndPorts"),
                ) if el is not None
            ])
        )

        return IOCDetail.Source(
            raw_data=raw_data,
            str_raw_confidence_score=(
                source_data.get("confidenceScore")
                if isinstance(source_data.get("confidenceScore"), str) else
                source_data.get("confidenceScore", {}).get("strRawConfidenceScore")
            ),
            addresses=addresses,
            source_url=source_data.get("sourceUrl"),
            category=source_data.get("category") or source_data.get("categorization"),
            first_active_time=(
                source_data.get("firstActiveTime") or
                source_data.get("activeTimerange", {}).get("start")
            ),
            last_active_time=(
                source_data.get("lastActiveTime") or
                source_data.get("activeTimerange", {}).get("end")
            ),
            raw_severity=source_data.get("rawSeverity"),
        )

    @staticmethod
    def build_siemplify_ioc_detail_source_addresses_obj(addresses):
        return [
            IOCDetail.Source.Address(raw_data=address, **address)
            for address in addresses
        ]

    @staticmethod
    def build_siemplify_asset_obj(asset_data):
        return Asset(
            asset_data,
            hostname=asset_data.get("asset", {}).get("hostname"),
            ip_address=asset_data.get("asset", {}).get("assetIpAddress"),
            first_seen_artifact_time=asset_data.get("firstSeenArtifactInfo", {}).get(
                "seenTime"
            ),
            last_seen_artifact_time=asset_data.get("lastSeenArtifactInfo", {}).get(
                "seenTime"
            ),
            **asset_data,
        )

    @staticmethod
    def build_siemplify_alert_obj(alert_data, alert_type=None, fallback_severity=None):
        raw_data = deepcopy(alert_data)
        alert_infos = [
            GoogleChronicleParser.build_siemplify_alert_info_obj(
                alert_info, alert_type, fallback_severity
            )
            for alert_info in alert_data.pop("alertInfos", [])
        ]

        return Alert(
            raw_data,
            hostname=alert_data.get("asset", {}).get("hostname"),
            ip_address=alert_data.get("asset", {}).get("assetIpAddress"),
            mac=alert_data.get("asset", {}).get("mac"),
            alert_infos=alert_infos,
            **alert_data,
        )

    @staticmethod
    def build_siemplify_alert_info_obj(
        alert_info_data, alert_type=None, fallback_severity=None
    ):
        return Alert.AlertInfo(
            raw_data=alert_info_data,
            alert_type=alert_type,
            fallback_severity=fallback_severity,
            **alert_info_data,
        )

    @staticmethod
    def extract_risk_score(first_detection: Dict[str, Any]) -> int:
        """
        Extracts the risk score from the detection dict.

        If the 'riskScore' field is missing or not an integer,
        a default risk score of 0 is returned.
        """
        raw_score = first_detection.get("riskScore")
        if isinstance(raw_score, int):
            return raw_score

        return 0

    @staticmethod
    def build_siemplify_event_obj(event_data):
        return Event(
            raw_data=event_data,
            event_type=event_data.get("metadata", {}).get("eventType"),
            product_name=event_data.get("metadata", {}).get("productName"),
            timestamp=event_data.get("metadata", {}).get("eventTimestamp"),
        )

    @staticmethod
    def build_detection(raw_data, fallback_severity=None):
        """Build detection """
        detections = raw_data.get("detection", [{}])
        first_detection = detections[0]
        risk_score = GoogleChronicleParser().extract_risk_score(first_detection)
        return Detection(
            raw_data=raw_data,
            identifier=raw_data.get("id"),
            rule_id=first_detection.get("ruleId"),
            alert_state=first_detection.get("alertState"),
            name=first_detection.get("ruleName"),
            created_time=raw_data.get("createdTime"),
            start_time=raw_data.get("timeWindow", {}).get("startTime"),
            end_time=raw_data.get("timeWindow", {}).get("endTime"),
            detections=detections,
            collection_elements=raw_data.get("collectionElements", []),
            rule_type=raw_data.get("type", ""),
            url_back_to_product=first_detection.get("urlBackToProduct"),
            rule_labels=first_detection.get("ruleLabels"),
            risk_score=risk_score,
            data_access_scope=raw_data.get("dataAccessScope"),
            fallback_severity=fallback_severity,
            outcomes=Outcomes.build_outcomes(first_detection.get("outcomes", [])),
            detection_depth=first_detection.get("detectionDepth"),
        )

    @staticmethod
    def build_chronicle_case_obj(case_data):
        return ChronicleCase(
            raw_data=case_data,
            id=str(case_data.get("case_id")),
            external_id=case_data.get("external_case_id", "") or "",
            priority=case_data.get("priority"),
            status=case_data.get("status"),
            environment=case_data.get("environment"),
            stage=case_data.get("stage"),
            has_failed=False,
            tracking_time=case_data.get("tracking_time"),
            display_name=case_data.get("title"),
        )

    @staticmethod
    def build_chronicle_alert_obj(alert_data):
        return ChronicleAlert(
            raw_data=alert_data,
            id=alert_data.get("alert_id"),
            siem_alert_id=alert_data.get("siem_alert_id", None),
            ticket_id=alert_data.get("ticket_id"),
            creation_time=alert_data.get("creation_time"),
            priority=alert_data.get("priority"),
            status=alert_data.get("status"),
            environment=alert_data.get("environment"),
            comment=alert_data.get("close_comment"),
            has_failed=False,
            tracking_time=alert_data.get("tracking_time"),
            reason=alert_data.get("close_reason"),
            root_cause=alert_data.get("close_root_cause"),
            case_id=alert_data.get("case_id"),
            group_id=alert_data.get("alert_group_id"),
            usefulness=alert_data.get("close_usefulness"),
        )

    @staticmethod
    def build_case_metadata_obj(raw_data):
        return CaseMetadata(
            raw_data=raw_data,
            id=raw_data.get("case_id"),
            tracking_time=raw_data.get("tracking_time"),
        )

    @staticmethod
    def build_alert_metadata_obj(raw_data):
        return AlertMetadata(
            raw_data=raw_data,
            group_id=raw_data.get("alert_group_id"),
            tracking_time=raw_data.get("tracking_time"),
        )

    @staticmethod
    def build_siem_event_obj(event_data):
        """Converts a raw SOAR event to Chronicle SIEM event of type SOAR."""
        return SiemEvent(
            raw_data=event_data,
            event_id=event_data.get("event_id"),
            start_time=event_data.get("start_time"),
            end_time=event_data.get("end_time"),
            event_time=event_data.get("event_time_epoch_time_in_ms"),
            receipt_time=event_data.get("receipt_time"),
            manager_receipt_time=event_data.get("manager_receipt_time"),
            event_message=event_data.get("message"),
            event_description=event_data.get("description"),
            source_user=event_data.get("source_user_name"),
            source_host=event_data.get("source_host_name"),
            source_domain=event_data.get("source_domain"),
            source_ip_address=event_data.get("source_address"),
            source_mac_address=event_data.get("source_mac_address"),
            source_user_id=event_data.get("source_user_id"),
            source_process_pid=event_data.get("source_process_name"),
            source_dns_domain=event_data.get("source_dns_domain"),
            source_nt_domain=event_data.get("source_nt_domain"),
            destination_user=event_data.get("destination_user_name"),
            destination_domain=event_data.get("destination_domain"),
            destination_host=event_data.get("destination_host_name"),
            destination_dns_domain=event_data.get("destination_dns_name"),
            destination_nt_domain=event_data.get("destination_nt_name"),
            destination_port=event_data.get("destination_port"),
            destination_ip_address=event_data.get("destination_address"),
            destination_process_pid=event_data.get("destination_process_name"),
            destination_uri=event_data.get("destination_url"),
            destination_mac_address=event_data.get("destination_mac_address"),
            generic_entity=event_data.get("generic_entity"),
            phone_number=event_data.get("phone_number"),
            email_subject=event_data.get("email_subject"),
            cve=event_data.get("cve"),
            threat_actor=event_data.get("threat_actor"),
            threat_campaign=event_data.get("threat_campaign"),
            threat_signature=event_data.get("threat_signature"),
            category_outcome=event_data.get("category_outcome"),
            deployment=event_data.get("deployment"),
            transport_protocol=event_data.get("transport_protocol"),
            application_protocol=event_data.get("application_protocol"),
            process_pid=event_data.get("process"),
            parent_process_pid=event_data.get("parent_process"),
            rule_generator=event_data.get("rule_generator"),
            file=event_data.get("file_name"),
            file_hash=event_data.get("file_hash"),
            file_type=event_data.get("file_type"),
            vendor=event_data.get("device_vendor"),
            product=event_data.get("device_product"),
            usb=event_data.get("usb"),
        )

    @staticmethod
    def build_siem_alert_obj(alert_data):
        """Converts a raw SOAR alert to Chronicle SIEM alert of type SOAR."""
        return SiemAlert(
            raw_data=alert_data,
            soar_alert_id=alert_data.get("alert_identifier"),
            start_time=alert_data.get("start_time"),
            end_time=alert_data.get("end_time"),
            detection_time=alert_data.get("detection_time"),
            source_system_uri=alert_data.get("source_system_url"),
            vendor=alert_data.get("vendor"),
            source_system=alert_data.get("source_system_name"),
            product=alert_data.get("product"),
            original_ticket_id=alert_data.get("ticket_id"),
            events=[
                GoogleChronicleParser.build_siem_event_obj(event)
                for event in alert_data.get("events")
            ],
            description=alert_data.get("name"),
            summary=alert_data.get("name"),
            alert_group_id=alert_data.get("alert_group_identifier"),
            soar_create_time=alert_data.get("creation_time"),
            environment=alert_data.get("environment"),
            has_failed=False,
            error_message=None,
        )

    @staticmethod
    def build_sync_result_from_raw_data(raw_data):
        """Builds a SOAR DTO which represents a new alert synchronization
        result from raw result of a SOAR API call."""
        return NewAlertSyncResult(
            alert_group_identifier=raw_data.get("alert_group_id"),
            environment=raw_data.get("environment"),
            creation_time=raw_data.get("creation_time"),
            created_in_siem=raw_data.get("created_in_siem"),
            siem_alert_id=raw_data.get("siem_alert_id"),
            message=raw_data.get("message"),
            updated_in_soar=raw_data.get("updated_in_soar"),
        )

    @staticmethod
    def build_sync_result_from_siem_alert(siem_alert):
        """Builds a SOAR DTO which represents a new alert synchronization
        result from a Chronicle SIEM alert of type SOAR."""
        return NewAlertSyncResult(
            alert_group_identifier=siem_alert.alert_group_id,
            environment=siem_alert.environment,
            creation_time=siem_alert.soar_create_time,
            created_in_siem=(not siem_alert.has_failed),
            siem_alert_id=siem_alert.siem_alert_id,
            message=siem_alert.error_message,
        )

    @staticmethod
    def parse_part_obj(raw_part) -> MultipartResponsePart | None:
        """Parser part object from multipart response."""
        conn = HTTPConnection("chronicle.dummy.com")
        conn.connect()
        response_ = HTTPResponse(conn.sock)
        response_.fp = BytesIO(raw_part)
        is_not_empty = seek_to_start(response_.fp)
        if is_not_empty < 0:
            return None

        response_.begin()
        return MultipartResponsePart(
            body=response_.read(),
            headers=response_.headers,
            status_code=response_.status
        )

    @staticmethod
    def parse_multipart_response(
            response: requests.Response,
    ) -> Iterator[MultipartResponsePart]:
        """ Parse multipart response.
        Args:
            response: requests.Response object

        Yields:
            requests.Response-like objects
        """
        boundary = (
            f"--{response.headers.get('Content-Type').split('boundary=')[-1]}"
        )
        # Read in chunks of approximately 10 MB to avoid using too much memory
        raw_parts = response.iter_lines(
            chunk_size=10 * MB_IN_BYTES,
            delimiter=boundary.encode("utf-8")
        )
        for raw_part in islice(raw_parts, 1, None):
            part_obj = GoogleChronicleParser.parse_part_obj(raw_part)
            if part_obj is not None:
                yield part_obj

    def build_udm_query_event_objects(self, raw_data):
        return [
            self.build_udm_query_event_object(item)
            for item in raw_data.get("events", normalize_stats_results(raw_data))
        ]

    @staticmethod
    def build_udm_query_event_object(raw_data):
        return UdmQueryEvent(raw_data=raw_data)

    @staticmethod
    def build_data_obj(raw_data):
        return ActionDetails(raw_data=raw_data)

    @staticmethod
    def build_rule_obj(raw_data):
        return Rule(raw_data=raw_data)

    def build_get_reference_list_data_obj(self, raw_data: list[SingleJson]) -> CaseData:
        return CaseData(
            raw_data=raw_data,
            getdata=([self.build_recommendation_object(item) for item in raw_data]),
        )

    def build_recommendation_object(self, item_data: SingleJson) -> RefDataObject:
        return RefDataObject(
            item_data,
            name=item_data.get("name", "").split("/")[-1],
            description=item_data.get("description", ""),
        )

    def build_reference_list_object(self, raw_data: SingleJson) -> ReferenceList:
        return ReferenceList(
            raw_data=raw_data,
            name=raw_data.get("name", "").split("/")[-1],
            description=raw_data.get("description", ""),
            lines=raw_data.get(
                "lines",
                [
                    value
                    for e in raw_data.get("entries", [])
                    if (value := e.get("value")) is not None
                ],
            ),
        )

    @staticmethod
    def build_retrohunt_object(raw_data: SingleJson) -> RetrohuntObject:
        return RetrohuntObject(raw_data=raw_data)

    @staticmethod
    def build_data_table_object(raw_data: SingleJson) -> DataTableDetails:
        return DataTableDetails.from_json(raw_data)

    @staticmethod
    def build_data_table_details_obj(raw_data: SingleJson) -> DataTableInfo:
        return DataTableInfo.from_json(raw_data)

    @staticmethod
    def build_added_data_table_row_obj(
        raw_data_list: list[SingleJson],
    ) -> list[AddedDataTableRow]:
        """Builds a list of AddedDataTableRow objects from a raw API response.

        Args:
            raw_data_list (list[SingleJson]): The raw list of row data from the API.

        Returns:
            list[AddedDataTableRow]: A list of parsed data table row objects.
        """
        if not isinstance(raw_data_list, list):
            return []
        return [AddedDataTableRow.from_json(item) for item in raw_data_list]

    def build_ask_gemini_object(self, raw_data: SingleJson)-> GeminiResponse:
        return GeminiResponse(raw_data=raw_data)

    @staticmethod
    def build_entity_summary_objects(
        raw_data_list: list[SingleJson],
    ) -> list[EntitySummary]:
        """Builds a list of EntitySummary objects from a list of raw JSON data.

        Args:
            raw_data_list (list[SingleJson]): A list of raw entity summary
                dictionaries from the API.

        Returns:
            list[EntitySummary]: A list of parsed EntitySummary objects.
        """
        return [EntitySummary.from_json(item) for item in raw_data_list]

    @staticmethod
    def build_detailed_entity_summary_object(
        combined_api_data: SingleJson,
        initial_summary_info: SingleJson | None = None,
    ) -> DetailedEntitySummary:
        """Builds a DetailedEntitySummary object from combined API data.

        This method takes the merged raw JSON data from both the alerts and
        prevalence summaries and, optionally, the initial summary information
        to create a comprehensive DetailedEntitySummary object.

        Args:
            combined_api_data (SingleJson): The raw JSON data combining alert
                and prevalence information for an entity.
            initial_summary_info (SingleJson | None): Optional. The raw data from
                an initial, less detailed summary call, used to enrich the final
                object.

        Returns:
            DetailedEntitySummary: A parsed object containing the detailed
                summary of the entity.
        """
        return DetailedEntitySummary.from_json(combined_api_data, initial_summary_info)

    @staticmethod
    def build_related_entities_response(
        raw_data: SingleJson,
    ) -> RelatedEntitiesResponse:
        """Builds a RelatedEntitiesResponse object from raw API data.

        This method parses the JSON response from the findRelatedEntities API
        endpoint into a structured RelatedEntitiesResponse object.

        Args:
            raw_data (SingleJson): The raw JSON data from the API response.

        Returns:
            RelatedEntitiesResponse: A parsed object containing the list of
                related entities and other response data.
        """
        return RelatedEntitiesResponse.from_json(raw_data)

    @staticmethod
    def build_watchlist_entities(
        raw_entities: list[SingleJson],
    ) -> list[WatchlistEntity]:
        return [WatchlistEntity.from_json(entity) for entity in raw_entities]

    def build_raw_logs(
        self,
        raw_json: SingleJson,
    ) -> list[RawLog]:
        """
        Builds a list of RawLog objects from the raw JSON response of the
        get_raw_logs_for_events API call.
        Args:
            raw_json: The raw JSON dictionary from the API.
        Returns:
            A list of RawLog data model objects.
        """
        return [RawLog.from_json(log_data) for log_data in raw_json.get("rawLogs", [])]

    def build_curated_rule_obj(
        self,
        raw_data,
    ) -> CuratedRule:
        """
        Build a CuratedRule object from raw data.
        Args:
            raw_data (dict): The raw data of the curated rule.
        Returns:
            (datamodels.CuratedRule): CuratedRule object.
        """
        return CuratedRule(raw_data=raw_data)
