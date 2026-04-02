from SiemplifyJob import SiemplifyJob
from SiemplifyUtils import output_handler

from TIPCommon.extraction import extract_action_param

from consts import (
    ALERTS_CREATOR_BATCH_SIZE,
    ALERTS_CREATOR_MAX_API_RETRIES,
    ALERTS_CREATOR_MAX_ITERATIONS,
    ALERTS_CREATOR_RETRY_TIME_DELTA_MS,
    ALERTS_CREATOR_SCRIPT_NAME,
)
from utils import retry_decorator, validate_alerts_creator_support
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2



class JobParametersParser:
    """This class parses the input parameters of the job."""

    def __init__(self, siemplify_):
        self.environment = JobParametersParser.parse_environment(siemplify_)
        self.api_root = JobParametersParser.parse_api_root(siemplify_)
        self.creds = JobParametersParser.parse_creds(siemplify_)
        self.verify_ssl = JobParametersParser.parse_verify_ssl(siemplify_)
        self.workload_identity_email = (
            JobParametersParser.parse_workload_identity_email(siemplify_)
        )

    @staticmethod
    def parse_environment(siemplify):
        return extract_action_param(
            siemplify=siemplify,
            param_name="Environment",
            is_mandatory=True,
            print_value=True,
            default_value="Default Environment",
        )

    @staticmethod
    def parse_api_root(siemplify):
        return extract_action_param(
            siemplify=siemplify,
            param_name="API Root",
            is_mandatory=True,
            print_value=True,
        )

    @staticmethod
    def parse_creds(siemplify):
        return extract_action_param(
            siemplify=siemplify,
            param_name="User's Service Account",
            is_mandatory=False,
            print_value=False,
        )

    @staticmethod
    def parse_verify_ssl(siemplify):
        return extract_action_param(
            siemplify=siemplify,
            param_name="Verify SSL",
            default_value=True,
            input_type=bool,
            print_value=True,
        )

    @staticmethod
    def parse_workload_identity_email(siemplify):
        return extract_action_param(
            siemplify=siemplify,
            param_name="Workload Identity Email",
            print_value=False,
        )


def log_fetched_alerts(siemplify, fetched_alerts):
    """Log fetched SOAR alerts group identifiers"""
    ids = [alert.get("alert_group_identifier") for alert in fetched_alerts]
    siemplify.LOGGER.info(f"Fetched the following SOAR alerts: {ids}")


def verify_soar_sync_results(siemplify, sync_results):
    """Count failed SOAR sync status updates and warn about them."""
    failed = 0
    for sync_result in sync_results:
        if not sync_result.updated_in_soar:
            siemplify.LOGGER.warn(
                "SOAR has failed updating the status of alert"
                f" {sync_result.alert_group_identifier}"
            )
        if not sync_result.created_in_siem or (
            sync_result.created_in_siem and not sync_result.updated_in_soar
        ):
            failed += 1

    return failed


@output_handler
def main():
    siemplify = SiemplifyJob()
    siemplify.script_name = ALERTS_CREATOR_SCRIPT_NAME
    siemplify.LOGGER.info("--------------- JOB STARTED ---------------")
    job_parameters_parser = JobParametersParser(siemplify)
    environments = (
        [job_parameters_parser.environment]
        if job_parameters_parser.environment
        else None
    )
    batch_size = ALERTS_CREATOR_BATCH_SIZE
    max_iterations = ALERTS_CREATOR_MAX_ITERATIONS
    siemplify.LOGGER.info("----------------- Main - Started -----------------")

    @retry_decorator(
        ALERTS_CREATOR_MAX_API_RETRIES,
        ALERTS_CREATOR_RETRY_TIME_DELTA_MS,
        siemplify.LOGGER
    )
    def fetch_new_alerts_to_sync(batch_size, environments):
        return siemplify.fetch_new_alerts_to_sync(batch_size, environments)

    @retry_decorator(
        ALERTS_CREATOR_MAX_API_RETRIES,
        ALERTS_CREATOR_RETRY_TIME_DELTA_MS,
        siemplify.LOGGER
    )
    def update_new_alerts_sync_status(request_sync_results, environments):
        return siemplify.update_new_alerts_sync_status(
            request_sync_results,
            environments
        )

    try:
        validate_alerts_creator_support(siemplify)
        manager = GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=job_parameters_parser.creds,
            workload_identity_email=job_parameters_parser.workload_identity_email,
            chronicle_soar=siemplify,
            api_root=job_parameters_parser.api_root,
            verify_ssl=job_parameters_parser.verify_ssl,
        )
        manager.test_connectivity()

        total_synced = 0

        for i in range(max_iterations):
            siemplify.LOGGER.info(f"Starting {i + 1}/{max_iterations} fetch attempt")
            siemplify.LOGGER.info(
                f"Fetching up to {batch_size} new alerts from the SOAR"
            )
            new_alerts = fetch_new_alerts_to_sync(batch_size, environments)

            new_alerts_count = len(new_alerts)
            siemplify.LOGGER.info(f"{new_alerts_count} SOAR alerts were fetched")
            if not new_alerts_count:
                siemplify.LOGGER.info("No new SOAR alerts were found. Stopping...")
                break
            log_fetched_alerts(siemplify, new_alerts)

            siemplify.LOGGER.info("Dispatching SOAR alerts to SIEM")
            request_soar_alerts = manager.convert_new_alerts_to_siem_alerts(new_alerts)
            response_soar_alerts = manager.batch_create_alerts_in_siem(
                request_soar_alerts
            )

            siemplify.LOGGER.info("Updating SOAR with SIEM response")
            request_sync_results = manager.convert_siem_alerts_to_sync_results(
                response_soar_alerts
            )
            response_sync_results = update_new_alerts_sync_status(
                request_sync_results, environments
            )
            sync_results = manager.build_new_alert_sync_results_from_response(
                response_sync_results
            )
            soar_failed_count = verify_soar_sync_results(siemplify, sync_results)
            total_synced += new_alerts_count - soar_failed_count

        siemplify.LOGGER.info(f"Total of {total_synced} alerts were synced in this run")
        siemplify.LOGGER.info("--------------- JOB FINISHED ---------------")

    except Exception as error:
        siemplify.LOGGER.error(f"Got exception on main handler. Error: {error}")
        siemplify.LOGGER.exception(error)
        raise


if __name__ == "__main__":
    main()
