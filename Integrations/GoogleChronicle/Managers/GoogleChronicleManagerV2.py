from __future__ import annotations

from typing import Any, Iterator

import copy
import datetime
import json
import uuid
from typing import Optional, List
from urllib.parse import urlparse, quote
import requests
import TIPCommon

from TIPCommon.types import SingleJson

import consts
import datamodels
import exceptions
import utils
from GoogleChronicleManager import GoogleChronicleManager


class GoogleChronicleManagerV2(GoogleChronicleManager):
    """Updated Chronicle Manager with 1Platform API support.

    This class extends GoogleChronicleManager and overwrites its methods to use new
    1Platform API endpoints.
    """

    @classmethod
    def create_manager_instance(
        cls,
        user_service_account: str | TIPCommon.types.SingleJson | None,
        chronicle_soar: TIPCommon.types.ChronicleSOAR,
        api_root: str = consts.API_URL,
        verify_ssl: bool = False,
        workload_identity_email: str | None = None,
        scopes: list[str] = consts.OAUTH_SCOPES,
    ):
        """
        Get Google Chronicle Manager object.

        Args:
            user_service_account (str | TIPCommon.types.SingleJson | None):
                Google Cloud Platform Service Account.
                if None, will try to create a manager using context data
            chronicle_soar (TIPCommon.types.ChronicleSOAR):
                Chronicle SOAR SDK object
            api_root (str, optional):
                Chronicle SIEM server API root.
                Defaults to `https://backstory.googleapis.com`.
            verify_ssl (bool, optional):
                Verify SSL certificate. Defaults to False.
            scopes: Authentication scopes
            workload_identity_email: str Workload Identity Email used for authentication

        Raises:
            exceptions.GoogleChronicleManagerError:
                If Service Account is Invalid

        Returns:
            GoogleChronicleManager:
                Google Chronicle Manager instance
        """
        if "backstory" in api_root:
            return GoogleChronicleManager.create_manager_instance(
                user_service_account,
                chronicle_soar,
                api_root,
                verify_ssl,
                workload_identity_email,
            )

        return super().create_manager_instance(
            user_service_account,
            chronicle_soar,
            api_root,
            verify_ssl,
            workload_identity_email,
            consts.OAUTH_SCOPES
        )

    def _get_full_url(self, url_id, **kwargs):
        """
        Get full url from url identifier.
        Args:
            url_id (str): The id of url
            kwargs (str): Variables passed for string formatting
        Returns:
            (str): The full url
        """
        api_root = (
            self.api_root if self.api_root.endswith("/")
            else f"{self.api_root}/"
        )
        return api_root + consts.ENDPOINTS_1PLATFORM[url_id].format(**kwargs)

    def _paginate_results(
        self,
        method: str,
        url: str,
        results_key: str,
        err_msg: str,
        params: dict | None = None,
        body: dict | None = None,
        next_page_token_key: str = "nextPageToken",
        page_token_param_name: str = "pageToken",
        limit: int | None = None,
    ) -> Iterator[dict]:
        """
        A generator to handle paginated API requests.

        Args:
            method (str): HTTP method (e.g., 'GET', 'POST').
            url (str): The API endpoint URL.
            results_key (str): The key in the JSON response that contains the list of
            results.
            err_msg (str): Error message to use if the request fails.
            params (dict | None): URL parameters for the request.
            body (dict | None): JSON body for the request.
            next_page_token_key (str): The key for the next page token.
            page_token_param_name (str): The name of the parameter for the page token.
            limit (int | None): The maximum number of items to return.

        Yields:
            Iterator[dict]: An iterator over the raw result items (dictionaries).
        """
        if params is None:
            params = {}

        count = 0
        page_token = None

        while True:
            current_params = params.copy()
            if page_token:
                current_params[page_token_param_name] = page_token

            try:
                response = self.session.request(
                    method,
                    url,
                    params=current_params,
                    json=body
                )
                self.validate_response(response, err_msg)
            except exceptions.GoogleChronicleAPILimitError as e:
                raise exceptions.GoogleChronicleAPILimitError(f"{err_msg}: {e}") from e

            except exceptions.GoogleChronicleManagerError as e:
                raise exceptions.GoogleChronicleManagerError(f"{err_msg}: {e}") from e

            response_json = response.json()
            results = response_json.get(results_key, [])

            if not isinstance(results, list):
                raise requests.exceptions.RequestException(
                    f"API response for paged results key '{results_key}' was not in the"
                    " expected list format."
                )

            if not results:
                break

            for item in results:
                if limit is not None and count >= limit:
                    return
                yield item
                count += 1

            page_token = response_json.get(next_page_token_key)
            if not page_token:
                break

    def test_connectivity(self) -> bool:
        """
        Test connectivity
        """
        try:
            self.get_reference_list(
                filter_value=None,
                filter_key="",
                filter_logic="",
                max_reference_list=1,
                expanded_details=False,
            )
            return True
        except exceptions.GoogleChronicleManagerError as e:
            raise exceptions.GoogleChronicleManagerError(
                "Unable to connect to Google Chronicle, please validate your "
                f"credentials: {e}"
            )

    def list_iocs(
        self,
        start_time: str,
        limit: Optional[int] = consts.LIMIT,
        fallback_severity=None,
        end_time: str = None,
    ) -> (bool, List[datamodels.IOC]):
        """List IoC Alerts discovered  within the specified time range.

        Args:
            start_time: {str} Start time for your request. Enter time using the
                time standard defined in RFC 3339. Time is represented by the span of
                UTC time since Unix epoch 1970-01-01T00:00:00Z.
            limit: {int} Specify the maximum number of IoCs to return. You can specify
                between 1 and 10,000.
            fallback_severity: {str} fallback severity for alerts
            end_time: {str} Start time for your request. Enter time using the time
                standard defined in RFC 3339. Time is represented by the span of
                UTC time since Unix epoch 1970-01-01T00:00:00Z.

        Returns:
            {(bool, [datamodels.IOC])} Tuple of a flag whether there are more results,
                and a list of found IOCs within the time range.
        """
        request_url = self._get_full_url("list_iocs")
        response = self.session.get(
            request_url,
            params={
                "timestampRange.start_time": start_time,
                "timestampRange.end_time": (
                    end_time if end_time is not None else
                    datetime.datetime.utcnow().strftime(consts.TIME_FORMAT)
                ),
                "maxMatchesToReturn": limit
            }
        )
        self.validate_response(response, "Unable to list IOCs")
        return response.json().get("moreDataAvailable", False), [
            self.parser.build_siemplify_ioc_obj(ioc, fallback_severity)
            for ioc in response.json().get("matches", [])
        ]

    def list_assets(
        self,
        start_time: str,
        end_time: str,
        ip: Optional[str] = None,
        domain: Optional[str] = None,
        file_hash: Optional[str] = None,
        limit: Optional[int] = consts.LIMIT,
    ):
        """
        List assets within the time range

        Args:
            start_time (str): start time of the time range
            end_time (str): end time of the time range
            ip (str): ip indicator for the asset
            domain (str): domain indicator for the asset
            file_hash (str): file hash indicator for the asset
            limit (int): maximum number of assets to return

        Returns:
            (str, [Asset]): tuple containing response uri and list of Asset objects
        """
        request_url = self._get_full_url("list_assets")
        params={
            "timestampRange.start_time": start_time,
            "timestampRange.end_time": end_time,
            "maxMatchesToReturn": limit,
        }

        if sum([ip is not None, domain is not None, file_hash is not None]) > 1:
            # More than 1 artifact was passed - invalid.
            raise exceptions.GoogleChronicleValidationError(
                "You can only specify a single artifact. "
                "The artifact indicator may either be a domain name, a destination "
                "IP address, or a file hash (one of MD5, SHA1, SHA256)."
            )
        if ip:
            params["fieldAndValue.value"] = ip
            params["fieldAndValue.valueType"] = "ASSET_IP_ADDRESS"

        elif domain:
            params["fieldAndValue.value"] = domain
            params["fieldAndValue.valueType"] = "DOMAIN_NAME"

        elif file_hash:
            params["fieldAndValue.value"] = file_hash
            params["fieldAndValue.valueType"] = consts.HASH_VALUE_TYPE_MAPPING.get(
                utils.get_hash_type(file_hash)
            )
        else:
            raise exceptions.GoogleChronicleValidationError(
                "You must specify at least one artifact. "
                "The artifact indicator may either be a domain name, a destination IP "
                "address, or a file hash (one of MD5, SHA1, SHA256)."
            )

        response = self.session.get(request_url, params=params)
        self.validate_response(response, "Unable to list assets")
        response_json = response.json()

        return response_json.get("uri", []), [
            self.parser.build_siemplify_ioc_obj(asset)
            for asset in response_json.get("matches", [])
        ]

    def list_events(
        self,
        start_time: str,
        end_time: str,
        reference_time: str,
        ip: Optional[str] = None,
        hostname: Optional[str] = None,
        mac: Optional[str] = None,
        limit: Optional[int] = consts.LIMIT,
        event_types: Optional[str] = None,
    ) -> tuple[str, list[datamodels.Event]]:
        """List events by running UDM query

        Args:
            start_time: {str} Start time for your request. Enter time using the time
                standard defined in RFC 3339. Time is represented by the span of UTC
                time since Unix epoch 1970-01-01T00:00:00Z.
            end_time: {str} End time for your request. Enter time using the time
                standard defined in RFC 3339. Time is represented by the span of UTC
                time since Unix epoch 1970-01-01T00:00:00Z.
            reference_time: {str} Specify the reference time for the asset you are
                investigating. Enter time using the time standard defined in RFC 3339.
                Time is represented by the span of UTC time since Unix epoch
                1970-01-01T00:00:00Z.
            ip: {str} Specify the ip indicator for the asset you are investigating.
            hostname: {str} Specify the hostname indicator for the asset you are
                investigating.
            mac: {str} Specify the mac indicator for the asset you are investigating.
            limit: {int} Specify the maximum number of events to return. You can
                specify between 1 and 10,000.
            event_types: {list} List of event types to return.

        Returns:
            {[datamodels.Event]} List of found events within the time range.
        """
        request_url = self._get_full_url("udm_search")
        query = utils.build_udm_query(ip, hostname, mac)

        params = {
            "time_range.start_time": start_time,
            "time_range.end_time": end_time,
            "query": query,
            "limit": limit,
        }

        response = self.session.get(
            request_url,
            params=params,
            timeout=consts.FIVE_MINUTES_IN_SECONDS
        )
        self.validate_response(response, "Unable to list events")
        response_json = response.json()

        events = [
            self.parser.build_siemplify_event_obj(event.get("udm", {}))
            for event in response_json.get("events", [])
        ]
        filtered_events = (
            [
                event
                for event in events
                if event.event_type.lower() in [t.lower() for t in event_types]
            ]
            if event_types
            else events
        )
        return response_json.get("uri", []), filtered_events

    def list_alerts(
        self,
        start_time: str,
        end_time: Optional[str] = None,
        limit: Optional[int] = consts.LIMIT,
        fetch_user_alerts: Optional[bool] = False,
        fallback_severity: Optional[str] = None,
    ):
        """This is an overwrite of the method defined in GoogleChronicleManager.

        The endpoint is currently not supported ->
        https://buganizer.corp.google.com/issues/407712702
        """
        return [], 0.0

    def get_ioc_details(
        self, ip: Optional[str] = None, domain: Optional[str] = None
    ) -> datamodels.IOCDetail | None:
        """Retrieve threat intelligence associated with an artifact indicator.

        The threat intelligence information is drawn from your enterprise security
        systems and from Google's IoC partners (for example, the DHS threat feed).
        You can only specify a single artifact. The artifact indicator may either be
        a domain name or an IP address.

        Args:
            ip: {str} Specify the ip indicator associated with the assets.
            domain: {str} Specify the domain indicator associated with the assets.

        Returns:
            {datamodels.IOCDetails} The found IOC detail for the given artifact.
        """
        if domain and ip:
            raise exceptions.GoogleChronicleValidationError(
                "You can only specify a single artifact. "
                "The artifact indicator may either be a domain name or an IP address."
            )

        if ip:
            params = {"artifactIndicator.destination_ip_address": ip}

        elif domain:
            params = {"artifactIndicator.domain": domain}

        else:
            raise exceptions.GoogleChronicleValidationError(
                "You must specify at least one artifact. "
                "The artifact indicator may either be a domain name or an IP address."
            )

        request_url = self._get_full_url("artifact_ioc_details")
        response = self.session.get(request_url, params=params)
        self.validate_response(response, f"Unable to get IOC details for {ip}")
        ioc_detail = response.json()
        if not ioc_detail:
            return None

        return self.parser.build_siemplify_ioc_detail_obj(ioc_detail)

    def get_events_by_query(
        self,
        query: str,
        start_time: str,
        end_time: Optional[str] = None,
        limit: Optional[int] = consts.LIMIT,
    ):
        raise NotImplementedError

    def get_reference_list(
        self,
        filter_value: str | None,
        filter_key: str,
        filter_logic: str,
        max_reference_list: int,
        expanded_details: bool,
    ) -> datamodels.RefDataObject | None:
        """Get Reference List

        Args:
            filter_value: Get the reference list name
            filter_key: Get the key that needs to be used to filter lists
            filter_logic: Get the filter logic either "Equal" or "Contains".
            max_reference_list: Get the reference lists to return. Default 100
            expanded_details: Get the boolean type value

        Returns:
            Reference data object
        """

        if expanded_details:
            list_view_details = consts.REFERENCE_LIST_VIEW_FULL
        else:
            list_view_details = consts.REFERENCE_LIST_VIEW_BASIC

        filter_key = consts.FILTER_KEY_MAPPING.get(
            filter_key,
            filter_key.lower()
        )
        result_data = []

        def _get_reference_list_all_view(
                params_: TIPCommon.types.SingleJson | None = None
        ) -> tuple[list[TIPCommon.types.SingleJson], str]:
            url = self._get_full_url(
                "get_reference_list_all_view", view=list_view_details
            )
            response = self.session.get(url, params=params_)
            self.validate_response(response)
            return (
                response.json().get("referenceLists", []),
                response.json().get("nextPageToken", "")
            )

        if filter_value is None:
            json_results, _ = _get_reference_list_all_view()
            result_data.extend(json_results)

        elif (
            filter_logic == consts.GET_REFERENCE_LIST_FILTER_LOGIC_EQUAL
            and filter_key == consts.GET_REFERENCE_FILTER_KEY_DISPLAY_NAME
        ):
            url = self._get_full_url(
                "get_reference_list",
                reference_list_name=filter_value,
                view=list_view_details,
            )
            response = self.session.get(url)
            self.validate_response(response)
            result_data.append(response.json())

        else:
            json_results, next_page_token = _get_reference_list_all_view()
            while next_page_token and len(result_data) <= max_reference_list:
                result_data.extend(
                    utils.get_reference_list_filter(
                        json_results, filter_key, filter_value, filter_logic
                    )
                )
                if len(result_data) >= max_reference_list:
                    result_data = result_data[:max_reference_list]
                    return self.parser.build_get_reference_list_data_obj(result_data)

                params = {"page_token": next_page_token}
                json_results, next_page_token = _get_reference_list_all_view(
                    params_=params
                )

            result_data.extend(
                utils.get_reference_list_filter(
                    json_results, filter_key, filter_value, filter_logic
                )
            )

        if len(result_data) <= 0:
            return None

        result_data = result_data[:max_reference_list]
        return self.parser.build_get_reference_list_data_obj(result_data)

    def get_reference_list_details(
        self, reference_list_name: str
    ) -> datamodels.ReferenceList:
        """Get reference list with full view

        Args:
            reference_list_name: Name of the reference list

        Returns:
            Reference list
        """
        request_url = self._get_full_url(
            "get_reference_list",
            reference_list_name=reference_list_name,
            view="REFERENCE_LIST_VIEW_FULL"
        )

        response = self.session.get(request_url)
        self.validate_response(response)

        return self.parser.build_reference_list_object(response.json())

    def add_value_to_reference_list(
        self, reference_list: datamodels.ReferenceList, values: set[str]
    ) -> datamodels.ReferenceList:
        """Add value to the reference list

        Args:
            reference_list: Reference List with the details
            values: Values that needs to be added to the reference list

        Returns:
            Updated Reference List after adding the values
        """
        entries = set(reference_list.lines)
        entries.update(values)
        payload = {"entries": [{"value": v} for v in entries]}

        if reference_list.content_type:
            payload.update({"syntaxType": reference_list.content_type})

        request_url = self._get_full_url(
            "update_reference_list",
            reference_list_name=reference_list.name
        )
        response = self.session.patch(request_url, json=payload)
        self.validate_response(response)

        return self.parser.build_reference_list_object(response.json())

    def remove_value_from_reference_list(
        self, reference_list: datamodels.ReferenceList, values: set[str]
    ) -> datamodels.ReferenceList:
        """Remove the values from the reference list

        Args:
            reference_list: Reference List with the details
            values: Values that needs to be removed from the reference list

        Returns:
            Updated Reference List after removing the values
        """
        entries = set(reference_list.lines).difference(values)
        payload = {"entries": [{"value": v} for v in entries]}

        if reference_list.content_type:
            payload.update({"syntaxType": reference_list.content_type})

        request_url = self._get_full_url(
            "update_reference_list",
            reference_list_name=reference_list.name
        )
        response = self.session.patch(request_url, json=payload)
        self.validate_response(response)

        return self.parser.build_reference_list_object(response.json())

    def execute_retrohunt(
        self, rule_id: str, start_time: str, end_time: str
    ) -> datamodels.ActionDetails:
        """Execute retrohunt

        Args:
            rule_id (str): rule id to fetch details for
            start_time (str): start time for the results
            end_time (str): end time for the results

        Returns:
            ActionDetails: ActionDetails object
        """
        url = self._get_full_url("execute_retrohunt", ruleId=rule_id)
        payload = {
            "process_interval": {
                "start_time": start_time,
                "end_time": end_time,
            }
        }

        response = self.session.post(url, json=payload)
        self.validate_response(response)
        return self.parser.build_retrohunt_object(response.json())

    def batch_update_cases_in_chronicle(self, cases_to_update):
        updated_cases = copy.deepcopy(cases_to_update)
        url_split = urlparse(self._get_full_url("batch_operation"))
        url = (
            url_split.scheme + "://" +
            url_split.netloc + "/" +
            url_split.path.split("/")[-1]
        )
        boundary = "===============7330845974216740156=="
        data = self.build_cases_batch_request_data(cases_to_update, boundary)
        response = self.session.post(
            url,
            data=data,
            headers={"content-type": f"multipart/mixed; boundary={boundary}"},
        )
        self.validate_response(response, "Unable to update cases")
        parsed_response_generator = self.parser.parse_multipart_response(response)
        for case, resp in zip(updated_cases, parsed_response_generator):
            try:
                if resp.status_code >= 400:
                    raise requests.HTTPError()
                case.external_id = resp.json().get("id")
            except requests.HTTPError:
                case.has_failed = True
                err = resp.json().get("error").get("message")
                self.chronicle_soar.LOGGER.error(
                    f"Failed to update case {case.id}. Reason: {err}"
                )

        return updated_cases

    def build_cases_batch_request_data(self, data_list, boundary):
        data_str = """
"""
        for item in data_list:
            payload = {
                "display_name": item.display_name,
                "soarPlatformInfo": {
                    "responsePlatformType": "RESPONSE_PLATFORM_TYPE_SIEMPLIFY",
                    "caseId": str(item.id),
                },
                "stage": item.stage,
                "priority": consts.PRIORITY_SIEMPLIFY_TO_CHRONICLE.get(
                    item.priority, 0
                ),
                "status": consts.STATUS_SIEMPLIFY_TO_CHRONICLE.get(item.status, 0),
            }
            if item.external_id in ["None", None, ""]:
                payload["id"] = item.external_id

            data_str += f"""--{boundary}
Content-Type: application/http
Content-Transfer-Encoding: binary

POST {urlparse(self._get_full_url("create_case")).path} HTTP/1.1
Content-Type: application/json
accept: application/json

{json.dumps({"case_resource": payload})}
"""
        final_boundary = f"""--{boundary}--
"""
        return data_str + final_boundary

    def build_alerts_batch_request_data(self, data_list, boundary):
        data_str = """
"""
        for item in data_list:
            alert_id = (
                item.siem_alert_id if item.siem_alert_id is not None else item.ticket_id
            )
            feedback = {
                "idp_user_id": consts.CHRONICLE_USER,
                "priority": consts.PRIORITY_SIEMPLIFY_TO_CHRONICLE.get(
                    item.priority, 0
                ),
                "status": consts.STATUS_SIEMPLIFY_TO_CHRONICLE.get(item.status, 0),
                "comment": item.comment,
                "reason": consts.REASON_SIEMPLIFY_TO_CHRONICLE.get(item.reason, 0),
                "root_cause": item.root_cause,
                "verdict": consts.SIEMPLIFY_REASON_TO_CHRONICLE_VERDICT.get(
                    item.reason, 0
                ),
                "reputation": consts.SIEMPLIFY_USEFULNESS_TO_CHRONICLE_REPUTATION.get(
                    item.usefulness, 0
                ),
            }
            feedback = {k: v for k, v in feedback.items() if v is not None}
            payload = {
                "alertId": alert_id,
                "responsePlatformInfo": {
                    "responsePlatformType": "RESPONSE_PLATFORM_TYPE_SIEMPLIFY",
                    "alertId": item.id,
                },
                "feedback": feedback,
                "caseName": item.case_id,
            }
            data_str += f"""--{boundary}
Content-Type: application/http
Content-Transfer-Encoding: binary

POST {urlparse(self._get_full_url("update_alert")).path} HTTP/1.1
Content-Type: application/json
accept: application/json

{json.dumps(payload)}
"""
        final_boundary = f"""--{boundary}--
"""

        return data_str + final_boundary

    def build_alerts_batch_create_request_data(
        self,
        soar_alerts: list[datamodels.SiemAlert],
        boundary: str
    ) -> tuple[str | None, list[datamodels.SiemAlert], list[datamodels.SiemAlert]]:
        """Generates a batch HTTP request in Chronicle format to create new SOAR
        alerts in SIEM.

        Args:
            soar_alerts: list of soar alert objects.
            boundry: A string to be used as a delimiter between the nested requests

        Returns:
            tuple containing
                1) Request payload for batch requests, containing each alert as a nested
                    request. If no alerts could be processed into the request, return
                    value will be `None`
                2) Orderd List of alerts that were successfully converted to requests
                3) List of alerts that could not be converted to requests
        """
        siem_alerts = []
        alert_payloads = []
        faulty_alerts = []
        for alert in soar_alerts:
            try:
                payload = {
                    "soarAlertId": alert.soar_alert_id,
                    "startTime": utils.convert_time_ms_to_siem_time(alert.start_time),
                    "endTime": utils.convert_time_ms_to_siem_time(alert.end_time),
                    "detectionTime": utils.convert_time_ms_to_siem_time(
                        alert.detection_time
                    ),
                    "sourceSystemUri": alert.source_system_uri,
                    "vendor": alert.vendor,
                    "sourceSystem": alert.source_system,
                    "product": alert.product,
                    "originalTicketId": alert.original_ticket_id,
                    "description": alert.description,
                    "summary": alert.summary,
                    "alertGroupId": alert.alert_group_id,
                    "soarCreateTime": utils.convert_time_ms_to_siem_time(
                        alert.soar_create_time
                    ),
                }
                events = []
                for event in alert.events:
                    raw_siem_event = {}
                    raw_siem_event["eventId"] = event.event_id
                    raw_siem_event["startTime"] = utils.convert_time_ms_to_siem_time(
                        event.start_time
                    )
                    raw_siem_event["endTime"] = utils.convert_time_ms_to_siem_time(
                        event.end_time
                    )
                    raw_siem_event["eventTime"] = utils.convert_time_ms_to_siem_time(
                        event.event_time
                    )
                    raw_siem_event["receiptTime"] = utils.convert_time_ms_to_siem_time(
                        event.receipt_time
                    )
                    raw_siem_event["managerReceiptTime"] = (
                        utils.convert_time_ms_to_siem_time(event.manager_receipt_time)
                    )
                    raw_siem_event["eventMessage"] = event.event_message
                    raw_siem_event["eventDescription"] = event.event_description
                    raw_siem_event["sourceUser"] = event.source_user
                    raw_siem_event["sourceHost"] = event.source_host
                    raw_siem_event["sourceDomain"] = event.source_domain
                    raw_siem_event["sourceIpAddress"] = event.source_ip_address
                    raw_siem_event["sourceMacAddress"] = event.source_mac_address
                    raw_siem_event["sourceUserId"] = event.source_user_id
                    raw_siem_event["sourceProcessPid"] = event.source_process_pid
                    raw_siem_event["sourceDnsDomain"] = event.source_dns_domain
                    raw_siem_event["sourceNtDomain"] = event.source_nt_domain
                    raw_siem_event["destinationUser"] = event.destination_user
                    raw_siem_event["destinationDomain"] = event.destination_domain
                    raw_siem_event["destinationHost"] = event.destination_host
                    raw_siem_event["destinationDnsDomain"] = (
                        event.destination_dns_domain
                    )
                    raw_siem_event["destinationNtDomain"] = event.destination_nt_domain
                    raw_siem_event["destinationPort"] = event.destination_port
                    raw_siem_event["destinationIpAddress"] = (
                        event.destination_ip_address
                    )
                    raw_siem_event["destinationProcessPid"] = (
                        event.destination_process_pid
                    )
                    raw_siem_event["destinationUri"] = event.destination_uri
                    raw_siem_event["destinationMacAddress"] = (
                        event.destination_mac_address
                    )
                    raw_siem_event["genericEntity"] = event.generic_entity
                    raw_siem_event["phoneNumber"] = event.phone_number
                    raw_siem_event["emailSubject"] = event.email_subject
                    raw_siem_event["cve"] = event.cve
                    raw_siem_event["threatActor"] = event.threat_actor
                    raw_siem_event["threatCampaign"] = event.threat_campaign
                    raw_siem_event["threatSignature"] = event.threat_signature
                    raw_siem_event["categoryOutcome"] = event.category_outcome
                    raw_siem_event["deployment"] = event.deployment
                    raw_siem_event["transportProtocol"] = event.transport_protocol
                    raw_siem_event["applicationProtocol"] = event.application_protocol
                    raw_siem_event["processPid"] = event.process_pid
                    raw_siem_event["parentProcessPid"] = event.parent_process_pid
                    raw_siem_event["ruleGenerator"] = event.rule_generator
                    raw_siem_event["file"] = event.file
                    raw_siem_event["fileHash"] = event.file_hash
                    raw_siem_event["fileType"] = event.file_type
                    raw_siem_event["vendor"] = event.vendor
                    raw_siem_event["product"] = event.product
                    raw_siem_event["usb"] = event.usb
                    raw_siem_event = {
                        key: value
                        for key, value in raw_siem_event.items()
                        if value is not None
                    }
                    events.append(raw_siem_event)
                payload["events"] = events
                alert_payloads.append(payload)
                siem_alerts.append(alert)
            except exceptions.InvalidTimeException as e:
                error_msg = f"Can not sync alert {alert.soar_alert_id}! {e}"
                self.siemplify_logger.error(
                    f"{error_msg}. "
                    f"Alert {alert.soar_alert_id} will be skipped..."
                )
                alert.has_failed=True
                alert.error_message=error_msg
                faulty_alerts.append(alert)
                continue

        if not siem_alerts:
            return None, [], faulty_alerts

        data_str = ""
        for payload in alert_payloads:
            data_str += f"""
--{boundary}
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: <b29c5de2-0db4-490b-b421-6a51b598bd22+1>

POST {urlparse(self._get_full_url("create_alert")).path} HTTP/1.1
Content-Type: application/json
accept: application/json

{json.dumps({"soar_alert": payload})}
"""
        return data_str + f"--{boundary}--\n", siem_alerts, faulty_alerts

    def data_table_details(
        self,
        data_table_identifier: str,
        action_name: str = "",
        expanded_rows: bool = False,
        max_data_table_rows: int = consts.MAX_DATA_TABLE_ROWS
    ) -> datamodels.DataTableInfo:
        """
        Fetches details of a specific data table.
        The identifier is typically the display name or resource ID suffix.
        API: GET /v1alpha/{instance_path}/dataTables/{data_table_identifier}

        Args:
            data_table_identifier (str): The identifier (e.g., display name) of the
            data table.
            action_name (str): An optional string indicating the calling action.
            If set to "GetDataTables", special handling for not-found responses and
            a specific parsing path is applied. Defaults to "".
            expanded_rows (bool): Whether to include row data in the result. Defaults
            to False.
            max_data_table_rows (int): The maximum number of rows to retrieve if
            expanded_rows is True. Defaults to `consts.MAX_DATA_TABLE_ROWS`

        Returns:
            Dict[str, any]: The JSON response containing data table details.
        """
        encoded_filter_value = quote(data_table_identifier)
        request_url = self._get_full_url(
            "get_data_table",
            data_table=encoded_filter_value
        )
        response = self.session.get(request_url)
        if action_name == "GetDataTables":
            if (
                response.status_code == requests.codes.not_found
                or (
                response.status_code == 400
                and "invalid argument" in response.text.lower()
                )
            ):
                self.chronicle_soar.LOGGER.info(
                    "No data tables were found for the provided criteria in"
                    " Google SecOps"
                )
                return None
            self.validate_response(response)
            table_json = response.json()
            if expanded_rows:
                all_rows_raw_data = []
                for i, row_obj in enumerate(
                    self.list_all_data_table_rows(data_table_identifier)
                ):
                    if i >= max_data_table_rows:
                        break
                    all_rows_raw_data.append(row_obj.raw_data)

                table_json["rows"] = utils.transform_data_table_rows(
                    all_rows_raw_data,
                    table_json.get("columnInfo", [])
                )

            return self.parser.build_data_table_object(table_json)

        self.validate_response(
            response,
            f"Failed to get details for data table '{data_table_identifier}'",
        )
        return self.parser.build_data_table_details_obj(response.json())

    def add_rows_to_data_table(
        self,
        data_table_identifier: str,
        parent_resource_name: str,
        individual_row_values_list: list[TIPCommon.types.SingleJson],
    ) -> list[datamodels.AddedDataTableRow]:
        """Adds multiple rows to a data table via bulk API.

        Uses 1Platform API: POST .../dataTables/.../dataTableRows:bulkCreate

        Args:
            data_table_identifier (str): Short ID of the data table for URL.
            parent_resource_name (str): Full resource name for payload.
            individual_row_values_list (list[dict]): Rows with {col: val}.
        Returns:
            list[datamodels.AddedDataTableRow]: Successfully added rows.
        """
        url = self._get_full_url("add_row", data_table=data_table_identifier)

        requests_payload = []
        for row_value_dict in individual_row_values_list:
            requests_payload.append(
                {"parent": parent_resource_name, "dataTableRow": row_value_dict}
            )

        bulk_api_payload = {"requests": requests_payload}

        try:
            response = self.session.post(url, json=bulk_api_payload)
            self.validate_response(
                response,
                f"Failed to add rows in bulk to data table "
                f"'{data_table_identifier}'",
            )
            response_json = response.json()

            created_rows = response_json.get(
                "dataTableRows", response_json.get("responses", [])
            )

            if not isinstance(created_rows, list):
                raise requests.exceptions.RequestException(
                    "API response for bulk adding rows was not in the "
                    "expected list format."
                )

            return self.parser.build_added_data_table_row_obj(created_rows)

        except exceptions.GoogleChronicleManagerError as req_e:
            raise exceptions.GoogleChronicleManagerError(
                f"Network error during bulk add to data table '{data_table_identifier}'"
                ": {req_e}"
            ) from req_e

    def list_all_data_table_rows(
        self,
        data_table_identifier: str,
        filter_query: str | None = None,
    ) -> Iterator[datamodels.AddedDataTableRow]:
        """A generator that yields all rows from a data table, handling pagination
        internally.

        Args:
            data_table_identifier: The display name of the data table.
            filter_query: Filter query to apply when retrieving rows.

        Yields:
            AddedDataTableRow: An object representing a row in the data table.
        """
        url = self._get_full_url("list_rows", data_table=data_table_identifier)
        params = {"page_size": consts.MAX_DATA_TABLE_PAGE_SIZE}
        if filter_query:
            params["filter"] = filter_query

        err_msg = (
            f"Failed to list rows from data table '{data_table_identifier}'"
        )

        raw_rows_iterator = self._paginate_results(
            method="GET",
            url=url,
            params=params,
            results_key="dataTableRows",
            page_token_param_name="pageToken",
            err_msg=err_msg,
        )

        for raw_row in raw_rows_iterator:
            parsed_rows = self.parser.build_added_data_table_row_obj([raw_row])
            if parsed_rows:
                yield parsed_rows[0]

    def get_data_table_rows(
        self,
        data_table_identifier: str,
        filter_query: str | None = None,
    ) -> datamodels.DataTableDetails:
        """Get all rows from a specific data table.

        Args:
            data_table_identifier: The display name of the data table.
            filter_query: Filter query to apply when retrieving rows.

        Returns:
            Data table rows details
        """
        all_rows = list(
            self.list_all_data_table_rows(
                data_table_identifier,
                filter_query=filter_query,
            )
        )

        return self.parser.build_data_table_object(
            {"dataTableRows": [row.raw_data for row in all_rows]}
        )

    def delete_data_table_row(
        self,
        data_table_identifier: str,
        row_id: str
    ) -> bool:
        """
        Delete a specific row from a data table by its ID.

        Args:
            data_table_identifier: data table name
            row_id: The ID of the row to delete

        """
        request_url = self._get_full_url(
            "delete_rows", data_table=data_table_identifier, data_table_row=row_id)
        response = self.session.delete(request_url)
        self.validate_response(
            response,
            f"Failed to delete row '{row_id}' from data table "
            f"'{data_table_identifier}'"
        )
        return True

    def get_all_data_tables(self) -> list[datamodels.DataTableDetails]:
        """ Retrieves a list of data tables, up to the specified maximum.

        Returns:
            List of DataTableDetails objects.
        """
        list_tables_url = self._get_full_url("list_data_tables")
        err_msg = "Failed to list data tables"

        raw_tables = self._paginate_results(
            method="GET",
            url=list_tables_url,
            results_key="dataTables",
            page_token_param_name="pageToken",
            err_msg=err_msg,
        )
        return [self.parser.build_data_table_object(table) for table in raw_tables]

    def enrich_data_table_with_rows(
        self,
        data_table: datamodels.DataTableDetails,
        max_data_table_rows: int,
    ) -> datamodels.DataTableDetails:
        """Populate rows into an existing DataTableDetails object.
        Args:
            data_table: DataTableDetails object to enrich with rows.
            max_data_table_rows: Maximum number of rows to retrieve and include.

        Returns:
            The same DataTableDetails object, now with rows populated.
        """
        raw_column_info_dicts = [col.raw_data for col in data_table.column_info]

        raw_row_dicts = []
        data_table_name = data_table.name.split("/")[-1]
        for i, row_obj in enumerate(self.list_all_data_table_rows(data_table_name)):
            if i >= max_data_table_rows:
                break
            raw_row_dicts.append(row_obj.raw_data)

        data_table.rows = [
            datamodels.RemovedDataTableRow.from_json(row_dict)
            for row_dict in utils.transform_data_table_rows(
                raw_row_dicts, raw_column_info_dicts
            )
        ]
        return data_table

    def opt_into_gemini(self, automatic_opt_in: bool) -> datamodels.GeminiResponse:
        """
        Enables or disables the Gemini chat feature for the user.

        Args:
            automatic_opt_in (bool): True to enable Gemini, False to disable.

        Returns:
            datamodels.GeminiResponse: An object representing the API response.
        """
        payload: dict[str, dict[str, bool]] = {
            "ui_preferences": {"enable_duet_ai_chat": automatic_opt_in}
        }
        request_url: str = self._get_full_url("opt_in")
        response: requests.Response = self.session.patch(request_url, json=payload)
        self.validate_response(response)
        return self.parser.build_ask_gemini_object(response.json())

    def create_conversation(self)-> datamodels.GeminiResponse:
        """
        Creates a new conversation with Gemini.

        A unique conversation name is generated automatically.

        Returns:
            datamodels.GeminiResponse: An object representing the API response,
                                     containing the new conversation details.
        """
        conversation_name: str = (
            f"Google SecOps SOAR - {uuid.uuid4()} - "
            f"{datetime.datetime.now().isoformat()}"
        )
        payload: dict[str, str] = {"display_name": conversation_name}
        request_url: str = self._get_full_url("create_conversation")
        response: requests.Response = self.session.post(request_url, json=payload)
        self.validate_response(response)

        return self.parser.build_ask_gemini_object(response.json())

    def execute_prompt(
        self,
        conversation_id: str,
        prompt: str
    )-> datamodels.GeminiResponse:
        """
        Send a message to the Gemini Chat.
        Args:
            conversation_id: The ID of the conversation.
            prompt: The message to send.
        Returns:
            Retrieves response from Gemini for the user's prompt.
        """
        payload: dict[str, dict[str, str]] = {"input": {"body": prompt}}
        request_url: str = self._get_full_url(
            "execute_prompt", conversation_id=conversation_id
        )
        response: requests.Response = self.session.post(request_url, json=payload)
        self.validate_response(response)
        return self.parser.build_ask_gemini_object(response.json())

    def delete_conversation(self, conversation_id: str)-> datamodels.GeminiResponse:
        """
        Delete a conversation.
        Args:
            conversation_id: The ID of the conversation to delete.
        Returns:
            Deletes the conversation ID.
        """
        request_url: str = self._get_full_url(
            "delete_conversation", conversation_id=conversation_id
        )
        params: dict[str, bool] = {"force": True}
        response: requests.Response = self.session.delete(request_url, params=params)
        self.validate_response(response)
        return self.parser.build_ask_gemini_object(response.json())

    def summarize_entities_from_query(
        self,
        query: str,
        start_time: str,
        end_time: str,
    ) -> list[datamodels.EntitySummary]:
        """
        Finds entities that match a UDM query and returns a summary for each.
        This is used to find the entity ID before fetching full details.

        Args:
            query (str): The UDM query to execute.
            start_time (str): The start of the time range in ISO 8601 format.
            end_time (str): The end of the time range in ISO 8601 format.

        Returns:
            list[datamodels.EntitySummary]: A list of EntitySummary objects found.
        """
        url: str = self._get_full_url("summarize_entities_from_query")
        params: dict[str, str] = {
            "query": query,
            "timeRange.startTime": start_time,
            "timeRange.endTime": end_time,
        }

        self.chronicle_soar.LOGGER.info(
            f"Requesting to summarize entities with query: {query}"
        )
        response: requests.Response = self.session.get(url, params=params)
        self.validate_response(
            response,
            "Failed to summarize entities from query"
        )

        summaries_payload: list[Any] = response.json().get("entitySummaries", [])
        actual_summaries: list[dict] = []

        if isinstance(summaries_payload, list):
            summary_group: Any
            for summary_group in summaries_payload:
                if not isinstance(summary_group, dict):
                    continue

                entity_list: list[Any] = summary_group.get("entity", [])
                if not isinstance(entity_list, list):
                    continue

                actual_summaries.extend(
                    item for item in entity_list if isinstance(item, dict)
                )

        if not actual_summaries and summaries_payload:
            self.chronicle_soar.LOGGER.error(
                "summarizeEntitiesFromQuery returned a payload that could not be "
                f"parsed into a list of summaries: {summaries_payload}"
            )

        return self.parser.build_entity_summary_objects(actual_summaries)

    def summarize_entity(
        self,
        entity_id: str,
        start_time: str,
        end_time: str,
        initial_summary_info: TIPCommon.types.SingleJson | None = None,
    ) -> datamodels.DetailedEntitySummary | None:
        """
        Returns a comprehensive summary of an entity by combining alerts and prevalence
        data.

        Args:
            entity_id (str): The unique identifier of the entity.
            start_time (str): The start of the time range in ISO 8601 format.
            end_time (str): The end of the time range in ISO 8601 format.
            initial_summary_info (SingleJson | None): The raw_data of the initial
            summary from summarizeEntitiesFromQuery.

        Returns:
            datamodels.DetailedEntitySummary: A DetailedEntitySummary object, or None
            if no data.
        """
        url: str = self._get_full_url("summarize_entity")

        alerts_params: dict[str, str | bool] = {
            "entityId": entity_id,
            "timeRange.startTime": start_time,
            "timeRange.endTime": end_time,
            "returnAlerts": True,
            "returnPrevalence": False,
            "includeAllUdmEventTypesForFirstLastSeen": True,
        }
        self.chronicle_soar.LOGGER.info(
            f"Requesting alerts summary for entity ID: {entity_id}"
        )
        alerts_response: requests.Response = self.session.get(url, params=alerts_params)
        self.validate_response(
            alerts_response,
            f"Failed to summarize entity alerts for {entity_id}"
        )
        alerts_data: TIPCommon.types.SingleJson = alerts_response.json()

        prevalence_params: dict[str, str | bool] = {
            "entityId": entity_id,
            "timeRange.startTime": start_time,
            "timeRange.endTime": end_time,
            "returnAlerts": False,
            "returnPrevalence": True,
            "includeAllUdmEventTypesForFirstLastSeen": True,
        }
        self.chronicle_soar.LOGGER.info(
            f"Requesting prevalence summary for entity ID: {entity_id}"
        )
        prevalence_response: requests.Response = self.session.get(
            url, params=prevalence_params
        )

        prevalence_data: TIPCommon.types.SingleJson
        if prevalence_response.status_code == 400:
            self.chronicle_soar.LOGGER.error(
                "Received status 400 when fetching prevalence data for entity "
                f"{entity_id}. This can happen if no prevalence data is available. "
                f"Continuing without it. Response: {prevalence_response.text}"
            )
            prevalence_data = {}
        else:
            self.validate_response(
                prevalence_response,
                f"Failed to summarize entity prevalence for {entity_id}",
            )
            prevalence_data = prevalence_response.json()

        final_combined_data: TIPCommon.types.SingleJson = utils.deep_merge_dicts(
            alerts_data, prevalence_data
        )

        if not final_combined_data:
            return None

        return self.parser.build_detailed_entity_summary_object(
            final_combined_data, initial_summary_info
        )

    def find_related_entities(
        self,
        entity_id: str,
        start_time: str,
        end_time: str,
    ) -> datamodels.RelatedEntitiesResponse:
        """
        Finds entities related to a given entity within a specified time range.

        Args:
            entity_id (str): The unique identifier of the entity.
            start_time (str): The start of the time range in ISO 8601 format.
            end_time (str): The end of the time range in ISO 8601 format.

        Returns:
            datamodels.RelatedEntitiesResponse: A RelatedEntitiesResponse object.
        """
        url: str = self._get_full_url("find_related_entities")
        params: dict[str, str | int | bool] = {
            "entityId": entity_id,
            "timeRange.startTime": start_time,
            "timeRange.endTime": end_time,
            "pageSize": 1000,
            "excludeFirstLastSeen": False,
        }

        self.chronicle_soar.LOGGER.info(
            f"Requesting to find related entities for ID: {entity_id}"
        )
        response: requests.Response = self.session.get(url, params=params)
        self.validate_response(
            response,
            f"Failed to find related entities for {entity_id}"
        )

        return self.parser.build_related_entities_response(response.json())

    def generate_udm_query(
        self,
        prompt: str
    ) -> TIPCommon.types.SingleJson:
        """Generate a UDM query based on the provided prompt.

        Args:
            prompt (str): The prompt to generate the UDM query from.

        Returns:
            TIPCommon.types.SingleJson: The JSON response containing the generated UDM
            query.
        """
        payload: dict[str, str] = {"text": prompt}
        request_url: str = self._get_full_url("generate_udm_query")
        response: requests.Response = self.session.post(request_url, json=payload)
        self.validate_response(response)

        return response.json()

    def get_watchlist_by_name(self, watchlist_name: str) -> datamodels.Watchlist | None:
        """
        Fetches a watchlist by its name.

        Args:
            watchlist_name (str): The name of the watchlist to fetch.

        Returns:
            datamodels.Watchlist: The watchlist object.
        """
        request_url: str = self._get_full_url("watchlists")
        results: list[TIPCommon.types.SingleJson] = self._paginate_results(
            method="GET",
            url=request_url,
            results_key="watchlists",
            err_msg="Failed to list watchlists",
        )
        watchlist: TIPCommon.types.SingleJson = next(
            (
                watchlist
                for watchlist in results
                if watchlist.get("displayName") == watchlist_name
            ),
            None,
        )
        if watchlist is not None:
            return datamodels.Watchlist.from_json(watchlist)

        return None

    def add_entry_to_watchlist(
        self,
        watchlist_id: str,
        formatted_entries: TIPCommon.types.SingleJson,
    ) -> list[datamodels.WatchlistEntity]:
        """Updates a watchlist by its ID.
        Args:
            watchlist_id (str): The ID of the watchlist to update.
            formatted_entries (TIPCommon.types.SingleJson): The entries to add to the
            watchlist, formatted as per API requirements.

        Returns:
            list[datamodels.WatchlistEntity]: The list of added watchlist entities.
        """
        request_url: str = self._get_full_url(
            "add_entry_to_watchlist",
            watchlist_id=watchlist_id,
        )
        payload: dict[str, TIPCommon.types.SingleJson] = {"requests": formatted_entries}
        response: requests.Response = self.session.post(request_url, json=payload)
        self.validate_response(
            response,
            f"Failed to update watchlist '{watchlist_id}'",
        )
        entities: list[TIPCommon.types.SingleJson] = response.json().get("entities", [])

        return self.parser.build_watchlist_entities(entities)

    def get_events_by_udm_query(
        self,
        query: str,
        start_time: str,
        end_time: str,
        limit: int,
    ) -> datamodels.UdmQueryEvent:
        """
        Executes a UDM query and returns the parsed events.

        Args:
            query (str): The UDM query string.
            start_time (str): The start of the time range in ISO 8601 format.
            end_time (str): The end of the time range in ISO 8601 format.
            limit (int): The maximum number of events to return.

        Returns:
            A tuple containing a UdmQueryEvent objects and the raw
            JSON response.
        """
        request_url: str = self._get_full_url("udm_search")
        params: SingleJson = {
            "query": query,
            "time_range.start_time": start_time,
            "time_range.end_time": end_time,
            "limit": limit
        }

        response: requests.Response = self.session.get(request_url, params=params)
        self.validate_response(response)
        raw_json_response: SingleJson = response.json()

        return self.parser.build_udm_query_event_objects(raw_json_response)

    def get_raw_logs_for_events(
        self,
        event_ids: list[str],
    ) -> list[datamodels.RawLog]:
        """
        Fetches raw logs in bulk for a given list of event IDs.

        Args:
            event_ids: A list of event IDs to fetch raw logs for.

        Returns:
            A list of RawLog objects containing the parsed log data.
        """
        request_url: str = self._get_full_url("find_raw_logs")
        params: SingleJson = {
            "ids": ",".join(event_ids),
            "caseSensitive": "true",
            "maxResponseByteSize": consts.MAX_RESPONSE_BYTE_SIZE
        }

        response: requests.Response = self.session.get(request_url, params=params)
        self.validate_response(response)

        return self.parser.build_raw_logs(response.json())
