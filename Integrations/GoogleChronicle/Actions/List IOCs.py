import datetime
from ScriptResult import EXECUTION_STATE_COMPLETED, EXECUTION_STATE_FAILED
from SiemplifyAction import SiemplifyAction
from SiemplifyUtils import output_handler

from TIPCommon.extraction import extract_action_param, extract_configuration_param
from TIPCommon.transformation import construct_csv

import consts
import exceptions
import utils
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2


SCRIPT_NAME = "List IoCs"


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

    start_time = extract_action_param(
        siemplify, param_name="Start Time", is_mandatory=False, print_value=True
    )
    limit = extract_action_param(
        siemplify,
        param_name="Max IoCs to Fetch",
        is_mandatory=False,
        print_value=True,
        default_value=consts.LIMIT,
        input_type=int,
    )

    if limit < 0:
        siemplify.LOGGER.info(
            '"Max IoCs to Fetch" must be non-negative. Using default of'
            f" {consts.LIMIT}."
        )
        limit = consts.LIMIT

    if not start_time:
        start_time = utils.datetime_to_rfc3339(
            datetime.datetime.utcnow() - datetime.timedelta(days=3)
        )

    siemplify.LOGGER.info("----------------- Main - Started -----------------")

    json_results = []
    status = EXECUTION_STATE_COMPLETED
    result_value = "true"

    try:
        manager = GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=creds,
            chronicle_soar=siemplify,
            api_root=api_root,
            verify_ssl=verify_ssl,
            workload_identity_email=workload_identity_email,
        )
        more_results_available, iocs = manager.list_iocs(
            start_time=start_time, limit=limit
        )
        json_results = [ioc.as_json() for ioc in iocs]

        siemplify.LOGGER.info(f"Found {len(iocs)} IOCs since {start_time}.")

        if iocs:
            siemplify.result.add_data_table(
                "IOCs", construct_csv([ioc.as_csv() for ioc in iocs])
            )

            if more_results_available:
                output_message = (
                    "Successfully fetch IoCs but there are still more IoCs"
                    " discovered in your Chronicle account. You might want to"
                    " narrow the time range and rerun the action to ensure you"
                    " have visibility on all possible IoCs."
                )
            else:
                output_message = (
                    "Successfully fetch IoCs discovered within your enterprise"
                    " within the specified time range."
                )

        else:
            output_message = (
                "No IoCs found within your enterprise for the specified time range."
            )

    except exceptions.GoogleChronicleAPILimitError as e:
        siemplify.LOGGER.error(
            "Failed to fetch IoCs due to reaching API request limitation."
            f" Error: {e}"
        )
        siemplify.LOGGER.exception(e)
        output_message = "Failed to fetch IoCs due to reaching API request limitation."
        status = EXECUTION_STATE_FAILED
        result_value = "false"

    except Exception as e:
        siemplify.LOGGER.error(f'Error executing action "{SCRIPT_NAME}". Reason: {e}')
        siemplify.LOGGER.exception(e)
        status = EXECUTION_STATE_FAILED
        result_value = "false"
        output_message = f'Error executing action "{SCRIPT_NAME}". Reason: {e}'

    siemplify.result.add_result_json(json_results)
    siemplify.LOGGER.info("----------------- Main - Finished -----------------")
    siemplify.LOGGER.info(f"Status: {status}:")
    siemplify.LOGGER.info(f"Result Value: {result_value}")
    siemplify.LOGGER.info(f"Output Message: {output_message}")
    siemplify.end(output_message, result_value, status)


if __name__ == "__main__":
    main()
