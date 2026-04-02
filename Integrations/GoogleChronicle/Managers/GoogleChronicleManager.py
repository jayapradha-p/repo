from __future__ import annotations

import copy
import datetime
import json
import sys
import time
from enum import Enum
from random import randint
from time import sleep
from typing import Iterator, List, Optional
from urllib.parse import urljoin, urlparse

import google.auth
import google.auth.credentials
import requests
import requests.adapters
from google.auth.compute_engine import _metadata
from google.auth.exceptions import RefreshError
from google.auth.transport.requests import AuthorizedSession, Request
from google.oauth2 import service_account


import TIPCommon.base.utils
import TIPCommon.types
from SiemplifyLogger import SiemplifyLogger
from TIPCommon.consts import NUM_OF_MILLI_IN_SEC
from TIPCommon.rest.auth import (
    get_impersonated_credentials,
    get_secops_siem_tenant_credentials,
)
from TIPCommon.smp_time import unix_now
from TIPCommon.types import SingleJson
from TIPCommon.utils import is_empty_string_or_none

import consts
import datamodels
import exceptions
import utils
from GoogleChronicleParser import GoogleChronicleParser


DEFAULT_RESULT_LIMIT = 10_000
DEFAULT_PAGE_SIZE = 100


class ListBasis(Enum):
    """Possible values for detection related requests ListBasis parameter"""

    DETECTION_TIME = "DETECTION_TIME"
    CREATED_TIME = "CREATED_TIME"


class GoogleChronicleManager:
    """
    Google Chronicle Manager
    """

    def __init__(
        self,
        api_root: str = consts.API_URL,
        credentials: google.auth.credentials.Credentials = None,
        verify_ssl: bool = False,
        chronicle_soar=None,
        **kwargs,
    ):
        """
        Create a Google Chronicle Manager object.

        Args:
            credentials (google.auth.credentials.Credentials):
                Google Cloud Platform Credentials object
            api_root (str, optional):
                Chronicle SIEM server URL root.
                Defaults to `https://backstory.googleapis.com`.
            verify_ssl (bool, optional):
                Verify SSL certificate. Defaults to False.
            chronicle_soar (ChronicleSoar, optional):
                Chronicle SOAR sdk object. Defaults to None.
        """
        if credentials is None and "type" in kwargs:
            credentials = self.from_servcie_account_legacy(**kwargs)
            chronicle_soar.LOGGER.warn(
                "You are using a legacy version of the integration job! "
                "Please update your job instance to the latest version!"
            )
        self.api_root = api_root
        self.session = AuthorizedSession(
            credentials, auth_request=self.prepare_auth_request(verify_ssl)
        )
        self.session.verify = verify_ssl
        self.parser = GoogleChronicleParser()
        self.chronicle_soar = chronicle_soar

    @property
    def siemplify_logger(self) -> SiemplifyLogger:
        return self.chronicle_soar.LOGGER

    @classmethod
    def create_manager_instance(
        cls,
        user_service_account: str | TIPCommon.types.SingleJson | None,
        chronicle_soar: TIPCommon.types.ChronicleSOAR,
        api_root: str = consts.API_URL,
        verify_ssl: bool = False,
        workload_identity_email: str | None = None,
        scopes: list[str] = consts.SCOPES,
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
            scopes: Authentication scopes
            verify_ssl (bool, optional):
                Verify SSL certificate. Defaults to False.
            workload_identity_email: str Workload Identity Email used for authentication

        Raises:
            exceptions.GoogleChronicleManagerError:
                If Service Account is Invalid

        Returns:
            GoogleChronicleManager:
                Google Chronicle Manager instance
        """
        if (
            is_empty_string_or_none(user_service_account)
            and is_empty_string_or_none(workload_identity_email)
        ):
            return cls.from_secops_context(
                chronicle_soar=chronicle_soar,
                api_root=api_root,
                scopes=scopes,
                verify_ssl=verify_ssl,
            )

        if not is_empty_string_or_none(workload_identity_email):
            return cls.from_workload_identity_email(
                workload_identity_email,
                chronicle_soar=chronicle_soar,
                api_root=api_root,
                scopes=scopes,
                verify_ssl=verify_ssl,
            )

        if isinstance(user_service_account, str):
            try:
                user_service_account = json.loads(user_service_account)
            except json.JSONDecodeError as e:
                raise exceptions.GoogleChronicleManagerError(
                    "Unable to parse credentials as JSON. Please validate creds"
                ) from e

        return cls.from_service_account_info(
            **user_service_account,
            api_root=api_root,
            scopes=scopes,
            verify_ssl=verify_ssl,
            chronicle_soar=chronicle_soar,
        )

    @staticmethod
    def from_servcie_account_legacy(
        type: str,
        project_id: str,
        private_key_id: str,
        private_key: str,
        client_email: str,
        client_id: str,
        auth_uri: str,
        token_uri: str,
        auth_provider_x509_cert_url: str,
        client_x509_cert_url: str,
        **kwargs,
    ):
        """Method to help create a amanager instance, in legacy way
        Should not be used, if possible, and the manager creation should be done with
        `create_manager_instance` method

        Args:
            type (str):
                GCP IAM principal type
            project_id (str):
                GCP principal project ID
            private_key_id (str):
                GCP principal private key ID
            private_key (str):
                GCP principal private key
            client_email (str):
                GCP principal client email
            client_id (str):
                GCP principal client ID
            auth_uri (str):
                GCP principal auth URI
            token_uri (str):
                GCP principal token URI
            auth_provider_x509_cert_url (str):
                GCP principal auth provider x509 cert URL
            client_x509_cert_url (str):
                GCP principal client x509 cert URL

        Returns:
            google.auth.credentials.Credentials:
                Credentials object matching the service account info
        """
        creds = {
            "type": type,
            "project_id": project_id,
            "private_key_id": private_key_id,
            "private_key": private_key,
            "client_email": client_email,
            "client_id": client_id,
            "auth_uri": auth_uri,
            "token_uri": token_uri,
            "auth_provider_x509_cert_url": auth_provider_x509_cert_url,
            "client_x509_cert_url": client_x509_cert_url,
            **kwargs,
        }

        return service_account.Credentials.from_service_account_info(
            info=creds, scopes=consts.SCOPES
        )

    @classmethod
    def from_service_account_info(
        cls,
        type: str,
        project_id: str,
        private_key_id: str,
        private_key: str,
        client_email: str,
        client_id: str,
        auth_uri: str,
        token_uri: str,
        auth_provider_x509_cert_url: str,
        client_x509_cert_url: str,
        api_root: str = consts.API_URL,
        verify_ssl: bool = False,
        chronicle_soar=None,
        scopes: str = consts.SCOPES,
        **kwargs,
    ):
        """Create a Google Chronicle Manager object from service account
        key info.

        Args:
            type (str):
                GCP IAM principal type
            project_id (str):
                GCP principal project ID
            private_key_id (str):
                GCP principal private key ID
            private_key (str):
                GCP principal private key
            client_email (str):
                GCP principal client email
            client_id (str):
                GCP principal client ID
            auth_uri (str):
                GCP principal auth URI
            token_uri (str):
                GCP principal token URI
            auth_provider_x509_cert_url (str):
                GCP principal auth provider x509 cert URL
            client_x509_cert_url (str):
                GCP principal client x509 cert URL
            api_root (str, optional):
                Chronicle SIEM server URL root.
                Defaults to `https://backstory.googleapis.com`.
            verify_ssl (bool, optional):
                Verify SSL certificate. Defaults to False.
            chronicle_soar (ChronicleSoar, optional):
                Chronicle SOAR sdk object. Defaults to None.
            scopes: Authentication scopes

        Returns:
            GoogleChronicleManager:
                Google Chronicle Manager instance
        """
        creds = {
            "type": type,
            "project_id": project_id,
            "private_key_id": private_key_id,
            "private_key": private_key,
            "client_email": client_email,
            "client_id": client_id,
            "auth_uri": auth_uri,
            "token_uri": token_uri,
            "auth_provider_x509_cert_url": auth_provider_x509_cert_url,
            "client_x509_cert_url": client_x509_cert_url,
            **kwargs,
        }

        credentials = service_account.Credentials.from_service_account_info(
            info=creds, scopes=scopes
        )
        return cls(api_root, credentials, verify_ssl, chronicle_soar)

    @classmethod
    def from_secops_context(
        cls,
        chronicle_soar: TIPCommon.types.ChronicleSOAR,
        api_root: str = consts.API_URL,
        scopes: list[str] = consts.SCOPES,
        verify_ssl: bool = False,
    ):
        """Create a Google Chronicle Manager object,
        using the Chronicle SOAR context of the SecOps Instance.

        Args:
            chronicle_soar (TIPCommon.types.ChronicleSOAR):
                Chronicle SOAR context
            api_root (str, optional):
                Chronicle SIEM server URL root.
                Defaults to `https://backstory.googleapis.com`.
            scopes: Authentication scopes
            verify_ssl (bool, optional):
                Verify SSL certificate. Defaults to False.

        Returns:
            GoogleChronicleManager:
                Google Chronicle Manager instance
        """
        credentials = get_secops_siem_tenant_credentials(
            chronicle_soar, target_scopes=scopes
        )
        manager = cls(api_root, credentials, verify_ssl, chronicle_soar)
        try:
            manager.test_connectivity()
        except exceptions.GoogleChronicleManagerError as e:
            raise exceptions.GoogleChronicleManagerError(
                "Authentication with Workload Identity to Google Chronicle "
                f"server resulted in failure. Error: {e}."
            ) from e
        return manager

    @classmethod
    def from_workload_identity_email(
            cls,
            workload_identity_email: str,
            chronicle_soar: TIPCommon.types.ChronicleSOAR,
            api_root: str = consts.API_URL,
            scopes: list[str] = consts.SCOPES,
            verify_ssl: bool = False,
    ):
        """Create a Google Chronicle Manager object,
        using the Chronicle SOAR context of the SecOps Instance.

        Args:
            workload_identity_email: Workload identity email
            chronicle_soar (TIPCommon.types.ChronicleSOAR):
                Chronicle SOAR context
            api_root (str, optional):
                Chronicle SIEM server URL root.
                Defaults to `https://backstory.googleapis.com`.
            scopes: Authentication scopes
            verify_ssl (bool, optional):
                Verify SSL certificate. Defaults to False.

        Returns:
            GoogleChronicleManager:
                Google Chronicle Manager instance
        """
        credentials = get_impersonated_credentials(
            target_principal=workload_identity_email,
            target_scopes=scopes
        )
        manager = cls(api_root, credentials, verify_ssl, chronicle_soar)
        try:
            manager.test_connectivity()

        except (exceptions.GoogleChronicleManagerError, RefreshError) as e:
            if consts.IMPERSONATION_ERROR_MESSAGE in str(e).lower():
                project_sa_email = GoogleChronicleManager._get_project_sa_email()
                if project_sa_email is not None:
                    raise exceptions.GoogleChronicleManagerError(
                        "Impersonation is not allowed for the provided service account "
                        f"{workload_identity_email}. Please add the "
                        '"Service Account Token Creator" role to the service '
                        f"account: {project_sa_email}"
                    ) from e

            raise exceptions.GoogleChronicleManagerError(
                "Authentication with Workload Identity to Google Chronicle "
                f"server resulted in failure. Error: {e}."
            ) from e

        return manager

    @staticmethod
    def _get_project_sa_email() -> str | None:
        sa_info: SingleJson = {}
        credentials, _ = google.auth.default()
        if hasattr(credentials, consts.SERVICE_ACCOUNT_EMAIL_KEY):
            sa_info = _metadata.get_service_account_info(
                Request(),
                service_account=credentials.service_account_email,
            )

        return sa_info.get("email")

    @staticmethod
    def prepare_auth_request(verify_ssl: bool = True):
        """
        Prepare an authenticated request.

        Note: This method is a duplicate of the same method in the
        GoogleCloudComputeManager class. The only change is
        that created session is using verify_ssl parameter to allow
        self-signed certificates.
        """
        auth_request_session = TIPCommon.base.utils.CreateSession.create_session()
        auth_request_session.verify = verify_ssl

        # Using an adapter to make HTTP requests robust to network errors.
        # This adapter retries HTTP requests when network errors occur
        # and the requests seems safely retryable.
        retry_adapter = requests.adapters.HTTPAdapter(max_retries=3)
        auth_request_session.mount("https://", retry_adapter)

        # Do not pass `self` as the session here, as it can lead to
        # infinite recursion.
        return Request(auth_request_session)

    def test_connectivity(self) -> bool:
        """
        Test connectivity
        """
        try:
            self.list_iocs(
                start_time=utils.datetime_to_rfc3339(datetime.datetime.utcnow()),
                limit=1,
            )
            return True
        except exceptions.GoogleChronicleManagerError as e:
            raise exceptions.GoogleChronicleManagerError(
                "Unable to connect to Google Chronicle, "
                f"please validate your credentials: {e}"
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
        return urljoin(self.api_root, consts.ENDPOINTS[url_id].format(**kwargs))

    def list_iocs(
        self,
        start_time: str,
        limit: Optional[int] = consts.LIMIT,
        fallback_severity=None,
    ) -> (bool, List[datamodels.IOC]):
        """
        List all the IoCs discovered within your enterprise within the specified time
        range. If you receive the maximum number of IoCs you specified using the limit
        parameter (or 10,000, the default),
        there might still be more IoCs discovered in your Chronicle account.
        You might want to narrow the time range and issue the call again to ensure you
        have visibility on all possible
        IoCs.
        :param start_time: {str} Start time for your request.
            Enter time using the time standard defined in RFC 3339.
            Time is represented by the span of UTC time since Unix epoch
            1970-01-01T00:00:00Z.
        :param limit: {int} Specify the maximum number of IoCs to return.
            You can specify between 1 and 10,000.
        :param fallback_severity: {str} fallback severity for alerts
        :return: {(bool, [datamodels.IOC])} Tuple of a flag whether there are more
            results, and a list of found IOCs within the time range.
        """
        request_url = f"{self.api_root}/v1/ioc/listiocs"
        response = self.session.get(
            request_url, params={"start_time": start_time, "page_size": limit}
        )
        self.validate_response(response, "Unable to list IOCs")
        return response.json().get("response", {}).get("moreDataAvailable", False), [
            self.parser.build_siemplify_ioc_obj(ioc, fallback_severity)
            for ioc in response.json().get("response", {}).get("matches", [])
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
        For your enterprise, given the specified artifact, list all the assets that
        accessed it within the specified time period, including the first and last time
        those assets accessed the artifact. This call returns a maximum
        of 100 assets per request. You can specify a narrower time period to reduce the
        number of assets returned.
        :param start_time: {str} Start time for your request.
            Enter time using the time standard defined in RFC 3339.
            Time is represented by the span of UTC time since Unix epoch
            1970-01-01T00:00:00Z.
        :param end_time: {str} End time for your request.
            Enter time using the time standard defined in RFC 3339.
            Time is represented by the span of UTC time since Unix epoch
            1970-01-01T00:00:00Z.
        :param ip: {str} Specify the ip indicator associated with the assets to
            filter by.
        :param domain: {str} Specify the domain indicator associated with the assets
            to filter by.
        :param ip: {str} Specify the file hash indicator associated with the assets
            to filter by.
        :param limit: {int} Specify the maximum number of assets to return.
            You can specify between 1 and 10,000.
        :return: {[datamodels.Asset]} List of found assets
            within the time range.
        """
        request_url = f"{self.api_root}/v1/artifact/listassets"
        params = {"start_time": start_time, "end_time": end_time, "page_size": limit}

        if sum([ip is not None, domain is not None, file_hash is not None]) > 1:
            # More than 1 artifacts was passed - invalid.
            raise exceptions.GoogleChronicleValidationError(
                "You can only specify a single artifact. "
                "The artifact indicator may either be a domain name, a destination IP"
                " address, or a file hash "
                "(one of MD5, SHA1, SHA256)."
            )
        elif ip:
            params["artifact.destination_ip_address"] = ip

        elif domain:
            params["artifact.domain_name"] = domain

        elif file_hash:
            params[utils.get_hash_type(file_hash)] = file_hash

        else:
            raise exceptions.GoogleChronicleValidationError(
                "You must specify at least one artifact. "
                "The artifact indicator may either be a domain name, a destination IP "
                "address, or a file hash "
                "(one of MD5, SHA1, SHA256)."
            )

        response = self.session.get(request_url, params=params)
        self.validate_response(response, "Unable to list assets")
        response_json = response.json()
        return response_json.get("uri", []), [
            self.parser.build_siemplify_asset_obj(asset)
            for asset in response_json.get("assets", [])
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
    ):
        """
        List all of the events discovered within your enterprise on a particular
        device within the specified time range.
        If you receive the maximum number of events you specified using the
        page_size parameter (or 10,000, the
        default), there might still be more events within your Chronicle account.
        You can narrow the time range and
        issue the call again to ensure you have visibility into all possible events.
        :param start_time: {str} Start time for your request.
            Enter time using the time standard defined in RFC 3339.
            Time is represented by the span of UTC time since Unix epoch
            1970-01-01T00:00:00Z.
        :param end_time: {str} End time for your request.
        Enter time using the time standard defined in RFC 3339.
            Time is represented by the span of UTC time since Unix epoch
            1970-01-01T00:00:00Z.
        :param reference_time: {str} Specify the reference time for the asset you are
            investigating.
            Enter time using the time standard defined in RFC 3339.
            Time is represented by the span of UTC time since Unix epoch
            1970-01-01T00:00:00Z.
        :param ip: {str} Specify the ip indicator for the asset you are investigating.
        :param hostname: {str} Specify the hostname indicator for the asset you are
            investigating.
        :param mac: {str} Specify the mac indicator for the asset you are investigating.
        :param limit: {int} Specify the maximum number of events to return.
            You can specify between 1 and 10,000.
        :param event_types: {list} List of event types to return.
        :return: {[datamodels.Event]} List of found events
            within the time range.
        """
        request_url = f"{self.api_root}/v1/asset/listevents"
        params = {
            "start_time": start_time,
            "end_time": end_time,
            "reference_time": reference_time or end_time,
            "page_size": limit,
        }

        if sum([ip is not None, hostname is not None, mac is not None]) > 1:
            # More than 1 artifacts was passed - invalid.
            raise exceptions.GoogleChronicleValidationError(
                "You can only specify a single indicator. "
                "The asset indicator may either be a hostname, "
                "an IP address or a MAC address."
            )
        elif ip:
            params["asset.asset_ip_address"] = ip

        elif hostname:
            params["asset.hostname"] = hostname

        elif mac:
            params["asset.mac"] = mac

        else:
            raise exceptions.GoogleChronicleValidationError(
                "You must specify at least one indicator. "
                "The asset indicator may either be a hostname, "
                "an IP address or a MAC address."
            )

        response = self.session.get(request_url, params=params)
        self.validate_response(response, "Unable to list events")
        response_json = response.json()
        events = [
            self.parser.build_siemplify_event_obj(event)
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
        """
        List all the events discovered within your enterprise on a particular device
        within the specified time range.
        If you receive the maximum number of events you specified using
        the page_size parameter (or 10,000, the
        default), there might still be more events within your Chronicle account.
        You can narrow the time range and
        issue the call again to ensure you have visibility into all possible events.
        :param start_time: {str} Start time for the time range in which the
            Alerts were discovered in RFC 3339.
        :param end_time: {str} End time for the time range in which the
            Alerts were discovered in RFC 3339.
        :param limit: {int} Specify the maximum number of alerts to return.
        You can specify between 1 and 100,000.
        :param fetch_user_alerts: {bool} Specifies if user alerts needs to be fetched
        :param fallback_severity: {str} fallback severity for alerts
        :return: {[datamodels.Alert]} List of found alerts
            within the time range.
        """
        request_url = self._get_full_url("list_alerts")
        params = {
            "start_time": start_time,
            "end_time": end_time
            or utils.datetime_to_rfc3339(datetime.datetime.utcnow()),
            "page_size": limit,
        }
        response, elapsed_time = self.retry_request(
            method="GET", request_url=request_url, params=params
        )
        self.validate_response(response, "Unable to list alerts")

        if fetch_user_alerts:
            return [
                self.parser.build_siemplify_alert_obj(
                    alert, consts.EXTERNAL_ALERT_ASSET_TYPE, fallback_severity
                )
                for alert in response.json().get("alerts", [])
            ] + [
                self.parser.build_siemplify_alert_obj(
                    alert, consts.EXTERNAL_ALERT_USER_TYPE, fallback_severity
                )
                for alert in response.json().get("userAlerts", [])
            ], elapsed_time

        return [
            self.parser.build_siemplify_alert_obj(alert)
            for alert in response.json().get("alerts", [])
        ], elapsed_time

    def get_ioc_details(
        self, ip: Optional[str] = None, domain: Optional[str] = None
    ) -> datamodels.IOCDetail | None:
        """
        Submit an artifact indicator and return any threat intelligence associated
        with that artifact.
        The threat intelligence information is drawn from your enterprise security
        systems and from Google's
        IoC partners (for example, the DHS threat feed).
        You can only specify a single artifact. The artifact indicator
        may either be a domain name or an IP address.
        :param ip: {str} Specify the ip indicator associated with the assets.
        :param domain: {str} Specify the domain indicator associated with the assets.
        :return: {datamodels.IOCDetails} The found IOC detail for the given artifact.
        """
        if domain and ip:
            raise exceptions.GoogleChronicleValidationError(
                "You can only specify a single artifact. "
                "The artifact indicator may either be a domain name or an IP address."
            )

        elif ip:
            params = {"artifact.destination_ip_address": ip}

        elif domain:
            params = {"artifact.domain_name": domain}

        else:
            raise exceptions.GoogleChronicleValidationError(
                "You must specify at least one artifact. "
                "The artifact indicator may either be a domain name or an IP address."
            )

        request_url = f"{self.api_root}/v1/artifact/listiocdetails"
        response = self.session.get(request_url, params=params)
        self.validate_response(response, f"Unable to get IOC details for {ip}")
        ioc_detail = response.json()
        if not ioc_detail:
            return None

        return self.parser.build_siemplify_ioc_detail_obj(ioc_detail)

    def get_rule_alerts(self, rule_id: str, start_time: str, end_time: str):
        """
        Get all the rule alerts discovered within your enterprise within the
        specified time range.
        :param rule_id: {str} IF of the rule.
        :param start_time: {str} Start time for your request.
            Enter time using the time standard defined in RFC 3339.
            Time is represented by the span of UTC time since Unix epoch
            1970-01-01T00:00:00Z.
        :param end_time: {str} End time for your request.
            Enter time using the time standard defined in RFC 3339.
            Time is represented by the span of UTC time since Unix epoch
            1970-01-01T00:00:00Z.
        :return: {[datamodels.Detection]} List of found detections.
        """
        request_url = self._get_full_url("rule_detections", ruleId=rule_id)
        limit = DEFAULT_RESULT_LIMIT
        params = {
            "start_time": start_time,
            "pageSize": limit,
            "end_time": end_time
            or utils.datetime_to_rfc3339(datetime.datetime.utcnow()),
        }
        response, elapsed_time = self.retry_request(
            method="GET", request_url=request_url, params=params
        )
        self.validate_response(response, "Unable to get rule alerts")

        results = response.json().get("detections", [])
        next_page_token = response.json().get("nextPageToken", "")

        while next_page_token:
            if len(results) >= limit:
                break

            params.update({"pageToken": next_page_token})
            response, total_seconds = self.retry_request(
                method="GET", request_url=request_url, params=params
            )
            self.validate_response(response, "Unable to get rule alerts")
            elapsed_time += total_seconds
            next_page_token = response.json().get("nextPageToken", "")
            results.extend(response.json().get("detections", []))

        return [
            self.parser.build_detection(detection) for detection in results
        ], elapsed_time

    def retry_request(self, method, request_url, params=None, body=None):
        """
        If received API limitation error, will retry the request given times
        :param method: {str} The method of the request (GET, POST, PUT, DELETE, PATCH)
        :param request_url: {str} The request url
        :param params: {dict} Parameters to use in the request
        :param body: {dict} The json payload of the request
        :return: {Response}
        """
        response = self.session.request(method, request_url, params=params, json=body)
        elapsed_time = response.elapsed.total_seconds()
        if response.status_code == consts.API_LIMIT_ERROR:
            for i in range(consts.MAX_RETRIES):
                sleep(randint(1, 3))
                response = self.session.request(
                    method, request_url, params=params, json=body
                )
                elapsed_time += response.elapsed.total_seconds()
                if response.status_code == consts.API_LIMIT_ERROR:
                    continue
                break
        return response, elapsed_time

    def get_events_by_query(
        self,
        query: str,
        start_time: str,
        end_time: Optional[str] = None,
        limit: Optional[int] = consts.LIMIT,
    ):
        """
        List all of the events discovered within your enterprise with the
        specified query.
        :param query: {str} Query that needs to be executed.
        :param start_time: {str} Start time for the time range in which the
            Events were discovered in RFC 3339.
        :param end_time: {str} End time for the time range in which the
            Events were discovered in RFC 3339.
        :param limit: {int} Specify the maximum number of events to return.
            You can specify between 1 and 100,000.
        :return: {list} List of found events within the time range.
        """
        request_url = f"{self.api_root}/v1/events/liststructuredqueryevents"
        params = {
            "start_time": start_time,
            "end_time": end_time
            or utils.datetime_to_rfc3339(datetime.datetime.utcnow()),
            "raw_query": query.replace("'", "'").replace('"', '"'),
            "page_size": limit,
        }
        response = self.session.get(request_url, params=params)
        if response.status_code == 400:
            raise exceptions.GoogleChronicleBadRequestError()

        self.validate_response(response, "Unable to fetch events")
        events = [
            self.parser.build_siemplify_event_obj(event.get("event", {}))
            for event in response.json().get("results", [])
        ]
        return events, response.elapsed.total_seconds()

    def build_api_query(self, activities, types, entity_identifier):

        queries = []
        activity_query = " or ".join(
            [f'metadata.event_type = "{activity}"' for activity in activities]
        )
        if activity_query:
            if len(activities) > 1:
                queries.append(f"({activity_query})")
            else:
                queries.append(f"{activity_query}")

        entity_query = " or ".join(
            [f'{type} = "{entity_identifier}"' for type in types]
        )
        if entity_query:
            if len(types) > 1:
                queries.append(f"({entity_query})")
            else:
                queries.append(f"{entity_query}")

        return " and ".join(queries)

    def get_events_by_udm_query(self, query, start_time, end_time, limit):
        """
        Get events by udm query
        Args:
            query (str): query to run
            start_time (str): start time
            end_time (str): end time
            limit (int): limit for results
        Returns:
            ([UdmQueryEvent]) list of UdmQueryEvent objects
        """
        url = self._get_full_url("udm_search")
        params = {
            "time_range.start_time": start_time,
            "time_range.end_time": end_time,
            "query": query,
            "limit": limit,
        }
        response = self.session.get(
            url,
            params=params,
            timeout=consts.FIVE_MINUTES_IN_SECONDS
        )
        self.validate_response(response, extract_error_details=True)
        return self.parser.build_udm_query_event_objects(response.json())

    def list_curated_rule_detections(
        self,
        curated_rule_id: str,
        start_time: str | None = None,
        end_time: str | None = None,
        list_basis: ListBasis = ListBasis.DETECTION_TIME,
        page_size: int = DEFAULT_PAGE_SIZE,
        result_limit: int = DEFAULT_RESULT_LIMIT,
    ) -> tuple[list[datamodels.Detection], float]:
        """Get detections by a curated rule

        Args:
            curated_rule_id:
            start_time: Start time of the time range to return detections for,
                filtering by the detection field specified in the list_basis
                parameter. If not specified, then detections are not limited
                by a lower bound.
            end_time: End time of the time range to return detections for,
                filtering by the detection field specified by the list_basis
                parameter. If not specified, then detections are not limited
                by an upper bound.
            list_basis: Sort detections by DETECTION_TIME or by CREATED_TIME.
                If not specified, defaults to DETECTION_TIME.
                Detections are returned in descending order of the timestamp.
            page_size: Specify the maximum number of detections to return
                (range is 1 through 1,000). The default is 100.
            result_limit: Limit the number of total results.

        Returns:

        """
        if not utils.is_curated_rule_id(curated_rule_id):
            raise ValueError("Rule ID must be a curated rule ID")

        url = self._get_full_url("list_curated_rule_detections", ruleId=curated_rule_id)
        params = {
            "start_time": start_time,
            "end_time": end_time
            or utils.datetime_to_rfc3339(datetime.datetime.now(datetime.timezone.utc)),
            "list_basis": list_basis.value,
            "page_size": page_size,
        }

        response, elapsed_time = self.retry_request(
            method="GET", request_url=url, params=params
        )

        error_msg = "Unable to get curated rule alerts"
        self.validate_response(response, error_msg)

        response_json = response.json()
        results = utils.get_curated_detections(response_json)

        next_page_token = response.json().get("nextPageToken", "")
        while next_page_token:
            if len(results) >= result_limit:
                break

            params.update({"pageToken": next_page_token})
            response, total_seconds = self.retry_request(
                method="GET", request_url=url, params=params
            )
            self.validate_response(response, error_msg)
            elapsed_time += total_seconds
            next_page_token = response.json().get("nextPageToken", "")

            response_json = response.json()
            results.extend(utils.get_curated_detections(response_json))

        if len(results) > result_limit:
            results = results[:result_limit]

        return (
            [self.parser.build_detection(detection) for detection in results],
            elapsed_time,
        )

    def get_rule_details(self, rule_id: str) -> datamodels.Rule:
        """Get Rule Details

        Args:
            rule_id: The Rule ID for which you want to fetch details

        Returns:
            Rule details
        """
        url = self._get_full_url("get_rule_details", ruleId=rule_id)
        response = self.session.get(url)
        self.validate_response(response)
        return self.parser.build_rule_obj(response.json())

    def get_curated_rule_details(
        self,
        rule_id: str,
    ) -> datamodels.CuratedRule:
        """Get Curated Rule Details

        Args:
            rule_id: The Rule ID for which you want to fetch details

        Returns:
            CuratedRule details
        """
        url: str = self._get_full_url("get_curated_rule_details")
        params: TIPCommon.types.SingleJson = {"filter": f'rule_id:"{rule_id}"'}
        response = self.session.get(url, params=params)
        self.validate_response(response)

        rules: list[TIPCommon.types.SingleJson]
        rules = response.json().get("featuredContentRules")
        if not rules:
            raise exceptions.GoogleChronicleNotFoundError(
                f"Curated rule with ID '{rule_id}' not found."
            )

        return self.parser.build_curated_rule_obj(rules[0])

    def get_detection_details(
        self, rule_id: str, detection_id: str
    ) -> datamodels.ActionDetails:
        """Get detection Details

        Args:
            rule_id: The rule ID for which you want to fetch details
            detection_id: The detection ID for which you want to fetch details

        Returns:
            Detection details
        """
        url = self._get_full_url(
            "get_detection_details", ruleId=rule_id, detection_id=detection_id
        )

        response = self.session.get(url)
        self.validate_response(response)
        return self.parser.build_data_obj(response.json())

    def execute_retrohunt(
        self, rule_id: str, start_time: str, end_time: str
    ) -> datamodels.ActionDetails:
        """Execute retrohunt

        Args:
            rule_id: Get Rule ID for which you want to fetch details
            start_time: Get Specify the start time for the results
            end_time: Get Specify the end time for the results

        Returns:
            Execute retrohunt details
        """
        url = self._get_full_url("execute_retrohunt", ruleId=rule_id)
        response = self.session.post(
            url, data={"startTime": start_time, "endTime": end_time}
        )
        self.validate_response(response)
        return self.parser.build_data_obj(response.json())

    def get_reference_list(
        self,
        filter_value: str,
        filter_key: str,
        filter_logic: str,
        max_reference_list: int,
        expanded_details: bool,
    ) -> datamodels.RefDataObject:
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
            list_view_details = "FULL"
        else:
            list_view_details = "BASIC"

        if filter_key == "Content Type":
            filter_key = consts.GET_REFERENCE_FILTER_KEY_CONTENT_TYPE
        else:
            filter_key = filter_key.lower()

        result_data = []

        if filter_value is None:
            url = self._get_full_url(
                "get_reference_list_all_view", view=list_view_details
            )
            response = self.session.get(url)
            self.validate_response(response)
            json_results = response.json().get("lists", [])
            result_data.extend(json_results)

        elif (
            filter_logic == consts.GET_REFERENCE_LIST_FILTER_LOGIC_EQUAL
            and filter_key == consts.GET_REFERENCE_LIST_FILTER_KEY_NAME
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
            url = self._get_full_url(
                "get_reference_list_all_view", view=list_view_details
            )
            response = self.session.get(url)
            self.validate_response(response)
            json_results = response.json().get("lists", [])
            next_page_token = response.json().get("nextPageToken", "")
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
                response = self.session.get(url, params=params)
                self.validate_response(response)
                next_page_token = response.json().get("nextPageToken", "")
                json_results = response.json().get("lists", [])

            result_data.extend(
                utils.get_reference_list_filter(
                    json_results, filter_key, filter_value, filter_logic
                )
            )

        if len(result_data) > 0:
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
            view="FULL"
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
        reference_list.lines.extend(values)

        payload = {"name": reference_list.name, "lines": reference_list.lines}

        if reference_list.content_type:
            payload.update({"contentType": reference_list.content_type})

        request_url = self._get_full_url("update_reference_list")
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
        lines = [value for value in reference_list.lines if value not in values]

        payload = {"name": reference_list.name, "lines": lines}

        if reference_list.content_type:
            payload.update({"contentType": reference_list.content_type})

        request_url = self._get_full_url("update_reference_list")
        response = self.session.patch(request_url, json=payload)
        self.validate_response(response)

        return self.parser.build_reference_list_object(response.json())

    @staticmethod
    def validate_response(
        response, error_msg="An error occurred", extract_error_details=False
    ):
        """ Validate http response from Chronicle SIEM API

        Args:
            response (requests.Response): The response object
            error_msg (str): The error message to display on failure
            extract_error_details (bool):
                specifies if details needs to be extracted from the response error
        """
        try:
            if response.status_code == consts.API_LIMIT_ERROR:
                raise exceptions.GoogleChronicleAPILimitError(
                    "Reached API request limitation"
                )

            response.raise_for_status()

        except requests.HTTPError as error:
            try:
                response.json()
                error = response.json().get("error", {})
                error_message = error.get("message", response.content)

                if response.status_code == 400:
                    raise exceptions.GoogleChronicleManagerError(
                        error.get("message", "")
                    )

                if response.status_code == 404:
                    raise exceptions.GoogleChronicleNotFoundError(
                        error.get("message", "")
                    )

                if extract_error_details:
                    error_details = "\n".join([
                        detail.get("detail", "") for detail in error.get("details", [])
                    ])

                    raise exceptions.GoogleChronicleManagerError(
                        f"{error_msg}: {error} {error_details or error_message}"
                    )

                error_content = (
                    response.json().get("error", {}).get("message", response.content)
                )
                raise exceptions.GoogleChronicleManagerError(
                    f"{error_msg}: {error} {error_content}"
                )

            except exceptions.GoogleChronicleManagerError:
                raise

            except:
                raise exceptions.GoogleChronicleManagerError(
                    f"{error_msg}: {error} {response.content}"
                )

    def _build_stream_detections_request_data(
            self,
            batch_size: int,
            page_token: str | None = None,
            page_start_time: str | None = None,
    ) -> TIPCommon.types.SingleJson:
        """Build stream detections request data,

        Args:
            batch_size: Batch size
            page_start_time: connector start time
            page_token: Next page token previously returned by API
        """
        req_data = {
            "detectionBatchSize": batch_size,
            "composite_alert_handling": "FLATTEN_EVENTS_ENTITIES"
        }

        if page_token:
            req_data["pageToken"] = page_token
        else:
            req_data["pageStartTime"] = page_start_time

        return req_data

    def stream_detection_alerts_in_connector(
        self,
        existing_ids: list[str],
        page_start_time: str,
        limit: int,
        python_process_timeout: int,
        connector_starting_time: int,
        timeout_threshold: float,
        page_token: str | None = None,
        fallback_severity: str | None = None,
    ):
        """
        Stream detection alerts in connector

        Args:
            existing_ids (list[str]): List of existing detection ids.
            limit: limit of alerts to process
            python_process_timeout: timeout for connector to fail
            connector_starting_time: connector start time
            timeout_threshold: timeout threshold for connector
            page_start_time: connector start time
            page_token: Next page token previously returned by API
            fallback_severity: severity level

        Returns:
            Processed alert detections
        """
        processed_detections = []
        batch_size = min(consts.MAX_DETECTION_STREAM_BATCH_SIZE, limit)
        req_data = self._build_stream_detections_request_data(
            batch_size,
            page_token,
            page_start_time,
        )

        (
            response_code,
            disconnection_reason,
            next_page_token,
            next_page_start_time,
            processed_detections,
        ) = self.stream_detection_alerts(
            existing_ids,
            req_data,
            processed_detections,
            limit,
            python_process_timeout,
            connector_starting_time,
            timeout_threshold,
            fallback_severity,
        )

        if next_page_token is not None:
            page_token = next_page_token
            page_start_time = None
        elif next_page_start_time is not None:
            page_token = None
            page_start_time = next_page_start_time
        else:
            self.chronicle_soar.LOGGER.info(
                disconnection_reason
                if disconnection_reason
                else "connection unexpectedly closed"
            )
            # We assume a disconnection was due to
            # invalid arguments if the connection
            # was refused with HTTP status code 400.
            if response_code == 400:
                raise RuntimeError(
                    f"connection refused due to invalid arguments {req_data}"
                )

        return page_token, page_start_time, processed_detections

    def stream_detection_alerts(
        self,
        existing_ids: list[str],
        req_data: TIPCommon.types.SingleJson,
        processed_detections: list[datamodels.Detection],
        limit: int,
        python_process_timeout: int,
        connector_starting_time: int,
        timeout_threshold: float,
        fallback_severity: str | None = None,
    ) -> tuple[int, str, str, str, list[datamodels.Detection]]:
        """Stream detections from Google Chronicle.

        Args:
            existing_ids (list[str]): List of already seen detections
            req_data (TIPCommon.types.SingleJson): Request data
            processed_detections (list) List to be populated with processed detections
            limit (int): Limit of detections to be fetched throughout all responses.
            python_process_timeout (int): Python script timeout
            connector_starting_time (int): Connector starting time UNIX
            timeout_threshold (float): Threshold for timeouts checks
            fallback_severity (str): Fallback severity to be set for detections

        Returns:
            Tuple containing status code, closure reason, next page token,
                next page start time and processed detections list
        """
        url = self._get_full_url("stream_detection_alerts")

        disconnection_reason = ""
        next_page_token = None
        next_page_start_time = None
        stream_timeout = max(
            consts.MIN_DETECTION_STREAM_TIMEOUT,
            int(python_process_timeout * timeout_threshold)
            - consts.SCRIPT_EXECUTION_MARGIN,
            # 10 seconds margin to ensure script execution ends gracefully
        )
        stream_deadline = unix_now() + stream_timeout * NUM_OF_MILLI_IN_SEC

        with self.session.post(
            url, stream=True, data=req_data, timeout=stream_timeout
        ) as response:
            self.chronicle_soar.LOGGER.info(
                f"Initiated connection to detection alerts stream with request: "
                f"{req_data}"
            )
            response_code = response.status_code

            if response.status_code != 200:
                disconnection_reason = (
                    "connection refused with "
                    + f"status={response.status_code}, error={response.text}"
                )
            else:
                for batch in self.parse_stream(response, stream_deadline):
                    if utils.is_approaching_timeout(
                        python_process_timeout,
                        connector_starting_time,
                        timeout_threshold,
                    ):
                        self.chronicle_soar.LOGGER.info(
                            "Timeout is approaching. Connector will gracefully exit."
                        )
                        break
                    if "error" in batch:
                        error_dump = json.dumps(batch["error"], indent="\t")
                        disconnection_reason = (
                            f"connection closed with error: {error_dump}"
                        )
                        break

                    if "heartbeat" in batch:
                        self.chronicle_soar.LOGGER.info(
                            "Got empty heartbeat (confirms connection/keepalive)"
                        )
                        continue

                    if "detections" not in batch:
                        next_page_token = batch.get("nextPageToken")
                        next_page_start_time = batch.get("nextPageStartTime")
                        self.chronicle_soar.LOGGER.info(
                            f"Got a nextPageToken={next_page_token} and "
                            f"nextPageStartTime={next_page_start_time}, "
                            f"no detections."
                        )
                        continue

                    new_detections = utils.filter_old_detections(
                        chronicle_soar=self.chronicle_soar,
                        detections=[
                            self.parser.build_detection(detection, fallback_severity)
                            for detection in batch.get("detections", [])
                        ],
                        existing_ids=existing_ids,
                        id_key="id",
                    )
                    self.chronicle_soar.LOGGER.info(
                        f"Got {len(new_detections)} new detections"
                    )
                    processed_detections.extend(new_detections)

                    if len(processed_detections) > limit:
                        self.chronicle_soar.LOGGER.info(
                            "Reached max number of alerts to be fetch in a cycle. "
                            "No more alerts will be fetched."
                        )
                        processed_detections = processed_detections[:limit]
                        break

                    next_page_token = batch.get("nextPageToken")
                    next_page_start_time = batch.get("nextPageStartTime")
                    self.chronicle_soar.LOGGER.info(
                        f"Got a nextPageToken={next_page_token} and"
                        f"nextPageStartTime={next_page_start_time}."
                    )

                    if len(processed_detections) == limit:
                        break

        return (
            response_code,
            disconnection_reason,
            next_page_token,
            next_page_start_time,
            processed_detections,
        )

    def parse_stream(
        self, response: requests.Response, stream_deadline: int
    ) -> Iterator[TIPCommon.types.SingleJson]:
        """Parse the response from the Google Chronicle.

        Args:
            response: The response object
            stream_deadline: The stream deadline, UNIX value in ms

        Yields:
            The parsed JSON response.
        """

        try:
            if response.encoding is None:
                response.encoding = "utf-8"

            pending = None

            start_time = time.time()
            for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
                if unix_now() >= stream_deadline:
                    raise TimeoutError

                if pending is not None:
                    chunk = pending + chunk

                lines = chunk.split("\r\n")

                if lines and lines[-1] and chunk and lines[-1][-1] == chunk[-1]:
                    pending = lines.pop()
                else:
                    pending = None

                for line in lines:
                    self.siemplify_logger.info(
                        f"It took {time.time() - start_time} seconds to fetch the new"
                        f" response with size - {sys.getsizeof(line)}."
                    )
                    start_time = time.time()
                    if not line or not ("{" in line and "}" in line):
                        continue

                    json_string = "{" + line.split("{", 1)[1].rsplit("}", 1)[0] + "}"
                    yield json.loads(json_string)

        except TimeoutError:
            self.siemplify_logger.info(
                "Timeout is approaching. Connector will gracefully exit."
            )
            yield {
                "error": {
                    "code": 500,
                    "status": "UNAVAILBLE",
                    "message": "Timeout is approaching. Connector will gracefully exit",
                }
            }

        except Exception as e:
            self.chronicle_soar.LOGGER.exception(e)
            yield {
                "error": {
                    "code": 500,
                    "status": "UNAVAILBLE",
                    "message": (
                        "exception caught while reading stream response (your streaming"
                        f" client should retry connection): {repr(e)}"
                    ),
                }
            }

    def get_updated_cases_metadata(
        self, siemplify, start_timestamp_unix_ms, count, allowed_environments, vendor
    ):

        results = siemplify.get_updated_sync_cases_metadata(
            start_timestamp_unix_ms=start_timestamp_unix_ms,
            count=count,
            allowed_environments=allowed_environments,
            vendor=vendor,
        )

        return [self.parser.build_case_metadata_obj(item.__dict__) for item in results]

    def get_updated_alerts_metadata(
        self,
        siemplify,
        start_timestamp_unix_ms,
        count,
        allowed_environments,
        vendor,
        include_non_synced_alerts,
    ):

        results = siemplify.get_updated_sync_alerts_metadata(
            start_timestamp_unix_ms=start_timestamp_unix_ms,
            count=count,
            allowed_environments=allowed_environments,
            vendor=vendor,
            include_non_synced_alerts=include_non_synced_alerts,
        )

        return [self.parser.build_alert_metadata_obj(item.__dict__) for item in results]

    def convert_siemplify_cases_to_chronicle(self, cases_with_details):

        return [
            self.parser.build_chronicle_case_obj(
                json.loads(json.dumps(case_data.__dict__))
            )
            for case_data in cases_with_details
        ]

    def convert_siemplify_alerts_to_chronicle(self, alerts_with_details, sync_cases):

        case_id_mappings = {case.case_id: case.external_case_id for case in sync_cases}
        self.chronicle_soar.LOGGER.info(f"case id mapping: {case_id_mappings}")
        for alert in alerts_with_details:
            setattr(alert, "case_id", case_id_mappings[alert.case_id])

        return [
            self.parser.build_chronicle_alert_obj(
                json.loads(json.dumps(alert_data.__dict__))
            )
            for alert_data in alerts_with_details
        ]

    def convert_new_alerts_to_siem_alerts(self, new_alerts_to_sync):
        """Converts a list of new alerts from the raw result
        of a SOAR API call to Chronicle SIEM alerts of type SOAR.
        """
        return [
            self.parser.build_siem_alert_obj(new_alert)
            for new_alert in new_alerts_to_sync
        ]

    def convert_siem_alerts_to_sync_results(self, soar_alerts):
        """Converts a list of Chronicle SIEM alerts of type SOAR
        to SOAR API DTO of new alerts synchronization results.
        """
        return [
            self.parser.build_sync_result_from_siem_alert(soar_alert).__dict__
            for soar_alert in soar_alerts
        ]

    def build_new_alert_sync_results_from_response(self, response):
        """Converts a list of raw SOAR synchronization results
        to SOAR API DTO of new alerts synchronization results.
        """
        return [
            self.parser.build_sync_result_from_raw_data(result) for result in response
        ]

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
                case.external_id = resp.json().get("name")
            except requests.HTTPError as e:
                case.has_failed = True
                err = resp.json().get("error").get("message")
                if consts.PERMISSION_ERROR_MESSAGE in err.lower():
                    raise exceptions.GoogleChroniclePermissionError(err) from e
                self.chronicle_soar.LOGGER.error(
                    f"Failed to update case {case.id}. Reason: {err}"
                )

        return updated_cases

    def batch_update_alerts_in_chronicle(self, alerts_to_update):
        updated_alerts = copy.deepcopy(alerts_to_update)
        url_split = urlparse(self._get_full_url("batch_operation"))
        url = (
            url_split.scheme + "://" +
            url_split.netloc + "/" +
            url_split.path.split("/")[-1]
        )
        boundary = "===============7330845974216740156=="
        data = self.build_alerts_batch_request_data(alerts_to_update, boundary)
        response = self.session.post(
            url,
            data=data,
            headers={"content-type": f"multipart/mixed; boundary={boundary}"},
        )
        self.validate_response(response, "Unable to update alerts")
        parsed_response_generator = self.parser.parse_multipart_response(response)
        for alert, resp in zip(updated_alerts, parsed_response_generator):
            try:
                if resp.status_code >= 400:
                    raise requests.HTTPError()
            except requests.HTTPError as e:
                alert.has_failed = True
                err = resp.json().get("error").get("message")
                if consts.PERMISSION_ERROR_MESSAGE in err.lower():
                    raise exceptions.GoogleChroniclePermissionError(err) from e
                self.chronicle_soar.LOGGER.error(
                    f"Failed to update alert {alert.id}. Reason: {err}"
                )

        return updated_alerts

    @utils.retry_decorator_class(
        consts.ALERTS_CREATOR_MAX_API_RETRIES,
        consts.ALERTS_CREATOR_RETRY_TIME_DELTA_MS,
        None,
        "siemplify_logger",
    )
    def batch_create_alerts_in_siem(
        self,
        alerts_to_create: list[datamodels.SiemAlert]
    ) -> list[datamodels.SiemAlert]:
        """Creates soar alerts in Chronicle SIEM tennat

        Args:
            alerts_to_create: list of alerts to create in SIEM

        Returns:
            list[datamodels.SiemAlert]: list of alerts containing creation status fields
        """

        url_split = urlparse(self._get_full_url("batch_operation"))
        url = (
                url_split.scheme + "://" +
                url_split.netloc + "/" +
                url_split.path.split("/")[-1]
        )
        boundary = "===============7330845974216740156=="
        data, sent_alerts, unsent_alerts = self.build_alerts_batch_create_request_data(
            alerts_to_create, boundary
        )
        if data:
            response = self.session.post(
                url,
                data=data,
                headers={"content-type": f"multipart/mixed; boundary={boundary}"},
            )
            self.validate_response(response, "Unable to create alerts")
            parsed_response_generator = self.parser.parse_multipart_response(response)
            for alert, resp in zip(sent_alerts, parsed_response_generator):
                try:
                    if resp.status_code >= 400:
                        alert.has_failed = True
                        alert.error_message = resp.json().get("error").get("message")
                        self.siemplify_logger.error(
                            f"Failed to create alert {alert.alert_group_id} in SIEM. "
                            f"Reason: {alert.error_message}"
                        )
                        if (
                            consts.PERMISSION_ERROR_MESSAGE
                            in alert.error_message.lower()
                        ):
                            raise exceptions.GoogleChroniclePermissionError(
                                alert.error_message
                            )
                        continue

                    alert.siem_alert_id = resp.json().get("name")
                    if not alert.siem_alert_id:
                        alert.has_failed = True
                        alert.error_message = (
                            f"Alert {alert.alert_group_id} was created in "
                            f"SIEM with null identifier"
                        )
                        self.siemplify_logger.error(
                            f"Failed to create alert {alert.alert_group_id} in SIEM. "
                            f"Reason: {alert.error_message}"
                        )
                except json.JSONDecodeError as e:
                    self.siemplify_logger.error(f"Failed parsing nested response! {e}")

            for alert in sent_alerts:
                if not alert.siem_alert_id and not alert.has_failed:
                    alert.has_failed = True
                    alert.error_message = "Failed to parse SIEM response"
                    self.siemplify_logger.error(
                        f"Failed to create alert {alert.alert_group_id} in SIEM. "
                        f"Reason: {alert.error_message}"
                    )

        processed_alerts = unsent_alerts + sent_alerts
        return processed_alerts

    def build_cases_batch_request_data(self, data_list, boundary):
        """Prepare batch create case request."""
        data_str = """
"""
        for item in data_list:
            payload = {
                "display_name": item.display_name,
                "responsePlatformInfo": {
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
                payload["name"] = item.external_id

            data_str += f"""--{boundary}
Content-Type: application/http
Content-Transfer-Encoding: binary

POST /v1/cases HTTP/1.1
Content-Type: application/json
accept: application/json

{json.dumps(payload)}
"""
        final_boundary = f"""--{boundary}--
"""
        return data_str + final_boundary

    def build_alerts_batch_request_data(self, data_list, boundary):
        """Build a batch create alerts request."""
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
                "id": alert_id,
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

PATCH /v1/alert/updatealert HTTP/1.1
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

POST /v1/soarAlerts HTTP/1.1
Content-Type: application/json
accept: application/json

{json.dumps(payload)}
"""
        return data_str + f"--{boundary}--\n", siem_alerts, faulty_alerts
