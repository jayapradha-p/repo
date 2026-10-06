from __future__ import annotations

import datetime

from typing import TYPE_CHECKING

from SiemplifyUtils import convert_datetime_to_unix_time, convert_unixtime_to_datetime

from TIPCommon.base.action.data_models import (
    CloseCaseOrAlertInconclusiveRootCauses,
    CloseCaseOrAlertMaliciousRootCauses,
    CloseCaseOrAlertNotMaliciousRootCauses,
)
from TIPCommon.base.job.base_sync_job import BaseSyncJob
from TIPCommon.base.job.job_case import (
    JobCase,
    SyncMetadata,
    JobCommentsResult,
    JobStatusResult,
)
from TIPCommon.data_models import CaseDataStatus, AlertCard

import constants
from datamodels import AlertWithEvidence
from Microsoft365DefenderManager import Microsoft365DefenderManager
from UtilsManager import (
    get_m365_alert_id_from_soar_alert,
    get_m365_alert_id_from_soar_alerts,
    parse_iso_datetime,
)

if TYPE_CHECKING:
    from typing import NoReturn, TypeAlias

    from TIPCommon.types import SingleJson


CaseIdModifiedTimeList: TypeAlias = list[tuple[str, int]]


class SyncAlerts(BaseSyncJob[Microsoft365DefenderManager]):
    def __init__(self) -> None:
        super().__init__(
            job_name=constants.SYNC_ALERTS_SCRIPT_NAME,
            context_identifier=constants.SYNC_ALERTS_IDENTIFIER,
            tags_identifiers=[constants.M365_DEFENDER_ALERT_TAG],
        )
        self.sync_limit = constants.CASES_SYNC_LIMIT
        self.manager: Microsoft365DefenderManager | None = None

    def _init_api_clients(self) -> None:
        """Initializes the API clients."""
        self.manager = Microsoft365DefenderManager(
            api_root=self.params.api_root,
            tenant_id=self.params.tenant_id,
            client_id=self.params.client_id,
            client_secret=self.params.client_secret,
            verify_ssl=self.params.verify_ssl,
            login_api_root=self.params.login_api_root,
            microsoft_graph_url=self.params.graph_api_root,
            siemplify=self.soar_job,
        )

    def modified_synced_case_ids_by_product(
        self,
        incident_ids: list[str],
        sorted_modified_ids: CaseIdModifiedTimeList,
    ) -> CaseIdModifiedTimeList:
        """Fetches modified alerts from Microsoft Defender and maps them to SecOps
        case IDs.

        Args:
            incident_ids (list[str]): A list of Microsoft Defender alert IDs that are
            associated with the SecOps cases to check for modifications.
            sorted_modified_ids (CaseIdModifiedTimeList): A list of tuples containing
            SecOps case IDs and their last modified times, sorted by time.

        Returns:
            CaseIdModifiedTimeList: A list of tuples containing SecOps case IDs and
            their last modified times.
        """
        product_ids_to_case_map = self.alert_ids_to_case_map_builder()
        modified_alerts = self._fetch_modified_alerts(incident_ids)
        filtered_alert_ids = self._filter_alert_ids(modified_alerts)
        new_modified_alerts = self._fetch_alerts_by_ids(filtered_alert_ids)

        return self._map_alerts_to_cases(
            new_modified_alerts,
            product_ids_to_case_map,
            sorted_modified_ids,
        )

    def _fetch_modified_alerts(self, alert_ids: list[str]) -> list[AlertWithEvidence]:
        """Fetches modified alerts from Microsoft Defender.

        Args:
            alert_ids (list[str]): A list of Microsoft Defender alert IDs to check for
            modifications.

        Returns:
            list[AlertWithEvidence]: A list of AlertWithEvidence datamodel objects
            representing the modified alerts.
        """
        return self.manager.get_alerts_by_ids(alert_ids)

    def _filter_alert_ids(self, modified_alerts: list[AlertWithEvidence]) -> list[str]:
        """Filters alert IDs to only those present in the modified alerts list.

        Args:
            modified_alerts (list[AlertWithEvidence]): A list of AlertWithEvidence
            datamodel objects representing the modified alerts.

        Returns:
            list[str]: A list of Microsoft Defender alert IDs that are present in the
            modified alerts list.
        """
        final_alert_ids = []

        for alert in modified_alerts:
            alert_timestamp = alert.raw_data.get("lastUpdateDateTime")
            modified_time = parse_iso_datetime(alert_timestamp)
            if modified_time > convert_unixtime_to_datetime(self.last_run_time):
                final_alert_ids.append(alert.alert_id)

        return final_alert_ids

    def _fetch_alerts_by_ids(self, alert_ids: list[str]) -> list[AlertWithEvidence]:
        """Fetches alerts by their IDs.

        Args:
            alert_ids (list[str]): A list of Microsoft Defender alert IDs to fetch.

        Returns:
            list[AlertWithEvidence]: A list of AlertWithEvidence datamodel objects
            representing the fetched alerts.
        """
        return self.manager.get_alerts_by_ids(alert_ids)

    def _map_alerts_to_cases(
        self,
        alerts: list[AlertWithEvidence],
        product_ids_to_case_map: dict[str, str],
        sorted_modified_ids: CaseIdModifiedTimeList,
    ) -> CaseIdModifiedTimeList:
        """Maps alerts to SecOps cases and determines the final modified time.

        Args:
            alerts (list[AlertWithEvidence]): A list of AlertWithEvidence datamodel
            objects representing the modified alerts.
            product_ids_to_case_map (dict[str, str]): A dictionary mapping Microsoft
            Defender alert IDs to SecOps case IDs.
            sorted_modified_ids (CaseIdModifiedTimeList): A list of tuples containing
            SecOps case IDs and their last modified times, sorted by time.

        Returns:
            CaseIdModifiedTimeList: A list of tuples containing SecOps case IDs and
            their last modified times.
        """
        results = []
        case_time_map = dict(sorted_modified_ids)

        for alert in alerts:
            alert_id = alert.alert_id
            case_id = product_ids_to_case_map.get(alert_id)

            if not case_id:
                self.logger.info(
                    f"Skipping alert sync for Defender alert ID {alert_id} "
                    "as no matching SecOps case/alert ID was found in the map."
                )
                continue

            modified_time_ms = self._get_alert_modified_time_ms(alert)
            case_time_ms = case_time_map.get(case_id, constants.DEFAULT_CASE_TIME)
            results.append((case_id, max(modified_time_ms, case_time_ms)))

        return results

    def _get_alert_modified_time_ms(self, alert: AlertWithEvidence) -> int:
        """Extracts the modified time from an alert and converts it to milliseconds.

        Args:
            alert (AlertWithEvidence): An AlertWithEvidence datamodel object
            representing the alert.

        Returns:
            int: The modified time in milliseconds.
        """
        modified_time_utc_str = alert.raw_data.get("lastUpdateDateTime")
        modified_time = parse_iso_datetime(modified_time_utc_str)

        return convert_datetime_to_unix_time(modified_time)

    def is_alert_and_product_closed(
        self,
        job_case: JobCase,
        product: AlertWithEvidence,
    ) -> bool:
        """Check if both the alert and the Microsoft Defender alert are closed.

        Args:
            job_case (JobCase): The SecOps case to check.
            product (AlertWithEvidence): The Microsoft Defender alert to check.

        Returns:
            bool: True if both the alert and the Microsoft Defender alert are closed,
            False otherwise.
        """
        alert = get_m365_alert_id_from_soar_alerts(self.soar_job, job_case)[
            product.alert_id
        ]

        if not alert:
            return False

        alert_closed = alert.status.lower() == "close"
        product_status = product.raw_data.get("status")
        product_closed = (
            product_status.lower() == constants.M365_STATUS_RESOLVED.lower()
        )

        return alert_closed and product_closed

    def _extract_product_ids_from_case(
        self,
        job_case: JobCase,
    ) -> list[str]:
        """Extracts product IDs from the SecOps case.

        Args:
            job_case (JobCase): The SecOps case to extract product IDs from.

        Returns:
            list[str]: A sorted list of unique product IDs extracted from the case.
        """
        alert_ids = list(
            get_m365_alert_id_from_soar_alerts(self.soar_job, job_case).keys()
        )
        return sorted(set(alert_ids))

    def alert_ids_to_case_map_builder(self) -> dict[str, str]:
        """Builds a map of Microsoft Defender alert IDs to SecOps case IDs.

        Returns:
            dict[str, str]: A dictionary mapping Microsoft Defender alert IDs to
            SecOps case IDs.
        """
        product_ids_to_case_map: dict[str, str] = {}
        for case_id, product_ids in self.processed_items.items():
            for product_id in product_ids:
                product_ids_to_case_map[product_id] = case_id

        return product_ids_to_case_map

    def map_product_data_to_case(self, job_case: JobCase) -> None:
        """Maps Defender Alert data into metadata.

        Args:
            job_case (JobCase): The SecOps case to map product data to.
        """
        mapping: dict[str, AlertCard] = get_m365_alert_id_from_soar_alerts(
            self.soar_job, job_case
        )
        product_ids_from_alerts = list(mapping.keys())
        job_case.product_ids_from_secops_alerts = mapping
        product_details = self._fetch_alerts_by_ids(product_ids_from_alerts)
        self._attach_comments_to_product_details(product_details)
        self._attach_product_details_to_case(job_case, product_details)
        self._populate_alert_metadata(job_case, product_details)
        self.remove_synced_data_from_db(job_case, product_details)

    def _attach_comments_to_product_details(
        self,
        product_details: list[AlertWithEvidence],
    ) -> None:
        """Attaches new comments to each product detail.

        Args:
            product_details (list[AlertWithEvidence]): A list of AlertWithEvidence
            datamodel objects representing the product details to attach comments to.
        """
        for product_detail in product_details:
            new_comments = self._get_new_m365_comments(product_detail)

            if isinstance(new_comments, list):
                product_detail.add_comments(new_comments)

    def _attach_product_details_to_case(
        self,
        job_case: JobCase,
        product_details: list[AlertWithEvidence],
    ) -> None:
        """Attaches product details to the SecOps case.

        Args:
            job_case (JobCase): The SecOps case to attach product details to.
            product_details (list[AlertWithEvidence]): A list of AlertWithEvidence
            datamodel objects representing the product details to attach to the case.
        """
        for product_detail in product_details:
            job_case.add_product_incident(product_detail, product_key="alert_id")

    def _populate_alert_metadata(
        self,
        job_case: JobCase,
        product_details: list[AlertWithEvidence],
    ) -> None:
        """Populates alert metadata for each alert in the case.

        Args:
            job_case (JobCase): The SecOps case to populate alert metadata for.
            product_details (list[AlertWithEvidence]): A list of AlertWithEvidence
            datamodel objects representing the product details to extract metadata from.
        """
        for product_detail in product_details:
            alert_identifier = job_case.get_alert_identifier_from_product_id(
                product_id=product_detail.alert_id,
            )

            job_case.alert_metadata[alert_identifier] = SyncMetadata(
                status=product_detail.raw_data.get("status"),
                assignee=product_detail.raw_data.get("assignedTo"),
                incident_number=product_detail.alert_id,
                closure_reason=product_detail.raw_data.get("classification"),
                determination=product_detail.raw_data.get("determination"),
            )

    def _get_new_m365_comments(self, m365_alert: AlertWithEvidence) -> list[str]:
        """Get new comments from a Microsoft Defender XDR Alert to be added to SOAR.

        Args:
            m365_alert: The Microsoft XDR Defender alert.

        Returns:
            list[str]: A list of new comments to be added to SOAR.
        """
        comments_to_add = []
        m365_comments: list = m365_alert.raw_data.get("comments", [])
        m365_comments.sort(key=lambda x: x.get("createdDateTime", ""))
        last_run_datetime = convert_unixtime_to_datetime(self.last_run_time)

        for comment in m365_comments:
            comment_text: str = comment.get("comment")

            if not comment_text or comment_text.startswith(
                constants.SECOPS_COMMENT_PREFIX
            ):
                continue

            comment_created_time: datetime.datetime = parse_iso_datetime(
                comment.get("createdDateTime")
            )

            if comment_created_time > last_run_datetime:
                comment_to_add_str: str = (
                    f"{constants.M365_COMMENT_PREFIX} {m365_alert.alert_id}: "
                    f"{comment_text}"
                )
                comments_to_add.append(comment_to_add_str)

        return comments_to_add

    def sync_status(self, job_case: JobCase) -> None:
        """Syncing status between Microsoft Defender alerts and SecOps cases/alerts.

        Args:
            job_case (JobCase): The SecOps case to sync status for.
        """
        res = job_case.get_status_to_sync(constants.M365_STATUS_RESOLVED)
        self._sync_product_status_to_case(res, job_case)
        self._sync_case_status_to_product(res, job_case)

    def _sync_product_status_to_case(
        self,
        res: JobStatusResult,
        job_case: JobCase,
    ) -> None:
        """Syncs Microsoft Defender alert status to SecOps case/alert status.

        Args:
            res (JobStatusResult): The result object containing status sync information.
            job_case (JobCase): The SecOps case to sync status for.
        """
        for alert, meta in res.alerts_to_close_in_soar:
            reason, root_cause = self._get_secops_closure_details(meta.closure_reason)
            comment = (
                f"{constants.M365_COMMENT_PREFIX}{meta.incident_number}: "
                "Alert was closed"
            )
            self.sync_product_status_to_case(
                job_case.case_detail.id_,
                alert.identifier,
                reason,
                root_cause,
                comment,
            )
            self._remove_synced_entries(
                synced_list=[(job_case.case_detail.id_, f"{meta.incident_number}")],
            )

    def _sync_case_status_to_product(
        self,
        res: JobStatusResult,
        job_case: JobCase,
    ) -> None:
        """Syncs SecOps case/alert status to Microsoft Defender alert status.

        Args:
            res (JobStatusResult): The result object containing status sync information.
            job_case (JobCase): The SecOps case to sync status for.
        """
        if not res.incidents_to_close_in_product:
            return

        for req in res.incidents_to_close_in_product:
            if req["is_case_closed"]:
                closure_reason = self.soar_job.get_case_closure_details(
                    [job_case.case_detail.id_]
                )[0].get("reason", "")
            else:
                closure_reason = req["reason"]

            classification, determination = self._get_m365_closure_details(
                closure_reason
            )
            comment = self.get_secops_closure_comment(job_case, req)
            comment = (
                f"{constants.SECOPS_COMMENT_PREFIX}{job_case.case_detail.id_}: "
                f"{comment}"
            )
            alert_id = req["meta"].incident_number
            self.manager.update_alert(
                alert_id,
                constants.M365_STATUS_RESOLVED,
                classification,
                determination,
            )
            self.manager.add_comment_to_alert(alert_id, comment)
            self.logger.info(
                "Successfully updated alert status "
                f"'{constants.M365_STATUS_RESOLVED}' for the alert "
                f"{alert_id}."
            )
            self._remove_synced_entries(
                synced_list=[(job_case.case_detail.id_, f"{alert_id}")],
            )

    def _get_secops_closure_details(self, m365_classification: str) -> tuple[str, str]:
        """Gets the SecOps case's/alert's closure details.

        Args:
            m365_classification (str): The classification of the Microsoft Defender
            alert.

        Returns:
            tuple[str, str]: A tuple containing the closure reason and root cause
            for SecOps.
        """
        if m365_classification == constants.CLASSIFICATION_TRUE_POSITIVE:
            return (
                constants.REASON_MALICIOUS,
                CloseCaseOrAlertMaliciousRootCauses.OTHER.value,
            )

        if m365_classification == constants.CLASSIFICATION_FALSE_POSITIVE:
            return (
                constants.REASON_NOT_MALICIOUS,
                CloseCaseOrAlertNotMaliciousRootCauses.OTHER.value,
            )

        return (
            constants.REASON_RESOLVED,
            CloseCaseOrAlertInconclusiveRootCauses.NO_CLEAR_CONCLUSION.value,
        )

    def _get_m365_closure_details(
        self,
        soar_closure_reason: str,
    ) -> tuple[str, str | None]:
        """Gets the Microsoft XDR Defender alert's closure details.

        Args:
            soar_closure_reason (str): The closure reason for the SecOps case/alert.

        Returns:
            tuple[str, str | None]: A tuple containing the classification and
            determination for the Microsoft Defender alert.
        """
        if soar_closure_reason == constants.REASON_MALICIOUS:
            return (constants.CLASSIFICATION_TRUE_POSITIVE, "maliciousUserActivity")

        if soar_closure_reason == constants.REASON_NOT_MALICIOUS:
            return (constants.CLASSIFICATION_FALSE_POSITIVE, "notMalicious")

        return (constants.CLASSIFICATION_OTHER, "other")

    def get_comments_to_sync(
        self,
        job_case: JobCase,
        product_comment_prefix: str,
        case_comment_prefix: str,
        product_incident_key="name",
    ) -> None:
        """Gets comments to sync between SecOps case and product alerts.

        Args:
            job_case (JobCase): The job case for which to sync comments.
            product_comment_prefix (str): The prefix for product comments.
            case_comment_prefix (str): The prefix for case comments.
            product_incident_key (str): The key for the product alert.
        """
        comments_to_sync = self.get_comment_to_sync(
            job_case,
            product_comment_prefix=product_comment_prefix,
            case_comment_prefix=case_comment_prefix,
            product_incident_key=product_incident_key,
        )

        return comments_to_sync

    def get_comment_to_sync(
        self,
        job_case: JobCase,
        product_comment_prefix: str,
        case_comment_prefix: str,
        product_incident_key="name",
    ) -> list[SingleJson]:
        """Gets comments to sync between SecOps case and product alerts.

        Args:
            job_case (JobCase): The job case for which to sync comments.
            product_comment_prefix (str): The prefix for product comments.
            case_comment_prefix (str): The prefix for case comments.
            product_incident_key (str): The key for the product alert.

        Returns:
            list[SingleJson]: A list of comments to sync.
        """
        case_comments_hashes = job_case.get_case_comments_hashes()
        product_comments_hashes = self.get_product_comments_hashes(job_case)

        product_comments_sync_to_case = self._get_product_comments_to_sync(
            job_case,
            product_comment_prefix,
            case_comment_prefix,
            product_incident_key,
            case_comments_hashes,
        )
        case_comments_sync_to_product = self._get_case_comments_to_sync(
            job_case,
            case_comment_prefix,
            product_comment_prefix,
            product_comments_hashes,
        )

        return JobCommentsResult(
            product_comments_sync_to_case=product_comments_sync_to_case,
            case_comments_sync_to_product=case_comments_sync_to_product,
        )

    def _get_product_comments_to_sync(
        self,
        job_case: JobCase,
        product_comment_prefix: str,
        case_comment_prefix: str,
        product_incident_key: str,
        case_comments_hashes: set,
    ) -> list[str]:
        """Gets product comments to sync to the SecOps case.

        Args:
            job_case (JobCase): The job case for which to sync comments.
            product_comment_prefix (str): The prefix for product comments.
            case_comment_prefix (str): The prefix for case comments.
            product_incident_key (str): The key for the product alert.
            case_comments_hashes (set): A set of hashes of the case comments for
            comparison.

        Returns:
            list[str]: A list of product comments to sync to the case.
        """
        product_comments_sync_to_case = []

        for alert in job_case.case_detail.alerts:
            if not self._is_valid_alert(alert):
                continue

            alert_identifier = alert.alert_group_identifier
            incident_identifier = getattr(alert.incident, product_incident_key)

            for product_comment in alert.incident.comments:
                comment_text = self._extract_comment_text(product_comment)
                comment_with_product_prefix = self._format_product_comment(
                    product_comment_prefix, incident_identifier, comment_text
                )
                comment_hash = job_case._generate_string_hash(
                    comment_with_product_prefix
                )
                if (
                    job_case._is_valid_product_comment(
                        comment_text, case_comment_prefix
                    )
                    and comment_hash not in case_comments_hashes
                ):
                    comment = f"{alert_identifier}: {comment_with_product_prefix}"
                    product_comments_sync_to_case.append(comment)

        return product_comments_sync_to_case

    def _is_valid_alert(self, alert: AlertCard) -> bool:
        """Checks if the SecOps alert is valid for comment syncing.

        Args:
            alert (AlertCard): The SecOps alert to check.

        Returns:
            bool: True if the alert is valid for comment syncing, False otherwise.
        """
        return hasattr(alert, "incident") and alert.incident is not None

    def _extract_comment_text(self, product_comment: str) -> str:
        """Extracts the text from a product comment.

        Args:
            product_comment (str): The product comment to extract text from.

        Returns:
            str: The extracted comment text.
        """
        raw_comment = str(product_comment).strip()

        if ":" in raw_comment:
            return raw_comment.rsplit(":", maxsplit=1)[-1].strip()

        return raw_comment

    def _format_product_comment(
        self,
        product_comment_prefix: str,
        incident_identifier: str,
        comment_text: str,
    ) -> str:
        """Formats a product comment with the appropriate prefix.

        Args:
            product_comment_prefix (str): The prefix for product comments.
            incident_identifier (str): The identifier for the product alert.
            comment_text (str): The text of the comment.

        Returns:
            str: The formatted product comment.
        """
        return f"{product_comment_prefix}{incident_identifier}: {comment_text}"

    def _get_case_comments_to_sync(
        self,
        job_case: JobCase,
        case_comment_prefix: str,
        product_comment_prefix: str,
        product_comments_hashes: set,
    ) -> list[str]:
        """Gets case comments to sync to the product.

        Args:
            job_case: The job case for which to sync comments.
            case_comment_prefix: The prefix for case comments.
            product_comment_prefix: The prefix for product comments.
            product_comments_hashes: A set of hashes of the product comments for
            comparison.

        Returns:
            list[str]: A list of case comments to sync to the product.
        """
        case_comments_sync_to_product = []
        for case_comment in job_case.case_comments:
            comment_text = case_comment["comment"]

            if product_comment_prefix in comment_text:
                continue

            comment_with_case_prefix = self._format_case_comment(
                case_comment_prefix, job_case.case_detail.id_, comment_text
            )
            comment_hash = job_case._generate_string_hash(comment_with_case_prefix)
            if (
                job_case._is_valid_secops_comment(case_comment, product_comment_prefix)
                and comment_hash not in product_comments_hashes
            ):
                case_comments_sync_to_product.append(comment_with_case_prefix)
        return case_comments_sync_to_product

    def _format_case_comment(
        self,
        case_comment_prefix: str,
        case_id: str,
        comment_text: str,
    ) -> str:
        """Formats a case comment with the appropriate prefix.

        Args:
            case_comment_prefix (str): The prefix for case comments.
            case_id (str): The identifier for the SecOps case.
            comment_text (str): The text of the comment.

        Returns:
            str: The formatted case comment.
        """
        return f"{case_comment_prefix}{case_id}: {comment_text}"

    def get_product_comments_hashes(self, job_case) -> list[str]:
        """Gets hashes of product comments for comparison.

        Args:
            job_case: The job case to extract product comment hashes from.

        Returns:
            list[str]: A list of hashes of the product comments.
        """
        comments_hashes = []

        for alert in job_case.case_detail.alerts:
            if not self._is_valid_alert(alert):
                continue
            for comment in alert.incident.comments:
                comments_hashes.append(
                    job_case._generate_string_hash(str(comment) or "")
                )

        return comments_hashes

    def sync_comments(self, job_case: JobCase) -> None:
        """Sync comments between SecOps and Microsoft Defender.

        Args:
            job_case (JobCase): The SecOps case to sync comments for.
        """
        if job_case.case_detail.status == CaseDataStatus.CLOSED:
            return

        comments_to_sync = self.get_comments_to_sync(
            job_case=job_case,
            product_comment_prefix=constants.M365_COMMENT_PREFIX,
            case_comment_prefix=constants.SECOPS_COMMENT_PREFIX,
            product_incident_key="alert_id",
        )
        self.sync_product_comments_to_case(
            case_id=job_case.case_detail.id_,
            comments=comments_to_sync.product_comments_sync_to_case,
        )
        self.sync_case_comments_to_product(
            job_case=job_case,
            comments=comments_to_sync.case_comments_sync_to_product,
        )

    def sync_case_comments_to_product(
        self,
        job_case: JobCase,
        comments: list[str],
    ) -> None:
        """Syncs SecOps comments to Microsoft Defender.

        Args:
            job_case (JobCase): The SecOps case to sync comments for.
            comments (list[str]): A list of comments to sync to Microsoft Defender.
        """
        for alert in self._get_unique_alerts(job_case):
            for block in self._chunk_comments(comments):
                self._push_comment_to_alert(alert, block)

    def _get_unique_alerts(self, job_case: JobCase) -> list[AlertCard]:
        """Gets open alerts from the job case.

        Args:
            job_case (JobCase): The SecOps case to extract alerts from.

        Returns:
            list[AlertCard]: A list of unique open AlertCard objects from the case.
        """
        unique_alerts = []

        for alert in job_case.case_detail.alerts:
            if not self._is_valid_alert(alert):
                continue
            if alert.incident.raw_data.get("status") == constants.M365_STATUS_RESOLVED:
                continue
            unique_alerts.append(alert)

        return unique_alerts

    def _chunk_comments(self, comments: list[str]) -> list[str]:
        """Chunks comments into blocks of maximum allowed characters.

        Args:
            comments (list[str]): A list of comments to chunk.

        Returns:
            list[str]: A list of comment blocks, each within the character limit.
        """
        blocks, current, length = [], [], 0

        for comment in comments:
            extra_length = len(comment) + (1 if current else 0)
            if length + extra_length > constants.MAX_CHARS:
                blocks.append("\n".join(current))
                current, length = [comment], len(comment)
            else:
                current.append(comment)
                length += extra_length

        if current:
            blocks.append("\n".join(current))

        return blocks

    def _push_comment_to_alert(self, alert: AlertCard, text: str) -> None:
        """Pushes a comment block to the alert.

        Args:
            alert (AlertCard): The alert to push the comment to.
            text (str): The comment text to push.
        """
        self.manager.add_comment_to_alert(alert.incident.alert_id, text)
        self.logger.info(
            "Successfully synced comments from SecOps to Defender alert "
            f"{alert.incident.alert_id}."
        )

    def sync_assignee(self, job_case: JobCase) -> None:
        """Defender -> SecOps Assignee Sync.

        Args:
            job_case (JobCase): The SecOps case to sync assignee for.
        """
        if (
            not self.params.sync_assignee
            or job_case.case_detail.status == CaseDataStatus.CLOSED
        ):
            return

        res = self.get_assignee_to_sync(job_case)

        if res.target_user:
            current_case_user = self.get_secops_assignee(job_case)
            secops_assignee = (
                current_case_user.raw_data.get("email")
                if current_case_user and current_case_user.raw_data
                else ""
            )

            if secops_assignee != res.target_user.get("email"):
                self.sync_assignee_to_case(
                    res.alert.identifier,
                    job_case.case_detail.id_,
                    res.target_user.get("displayName"),
                )

    def sync_severity(self, job_case: JobCase) -> None:
        """Defender -> SecOps Priority Sync.

        Args:
            job_case (JobCase): The SecOps case to sync severity for.
        """

    def sync_tags(self, job_case: JobCase) -> None:
        """Bidirectional Tag Sync.

        Args:
            job_case (JobCase): The SecOps case to sync tags for.
        """

    def remove_synced_data_from_db(
        self,
        job_case: JobCase,
        product_details: list[AlertWithEvidence],
    ) -> None:
        """
        Removes synced entries from the DB if both the case alert and the product alert
        are closed.

        Args:
            job_case (JobCase): The SecOps case to check for closed alerts.
            product_details (list[AlertWithEvidence]): A list of AlertWithEvidence
            datamodel objects representing the product details to check for
            closed status.
        """
        for alert in job_case.case_detail.alerts:
            alert_id = get_m365_alert_id_from_soar_alert(self.soar_job, alert)
            matching_product = next(
                (p for p in product_details if p.alert_id == alert_id),
                None,
            )

            if not matching_product:
                continue

            case_id = job_case.case_detail.id_
            alert_id = f"{matching_product.alert_id}"
            entry = (case_id, alert_id)

            if self.is_alert_and_product_closed(job_case, matching_product):
                self._remove_synced_entries([entry])


def main() -> NoReturn:
    SyncAlerts().start()


if __name__ == "__main__":
    main()
