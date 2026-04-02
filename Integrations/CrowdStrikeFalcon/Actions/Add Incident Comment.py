from SiemplifyAction import SiemplifyAction
from SiemplifyUtils import output_handler
from ScriptResult import EXECUTION_STATE_COMPLETED, EXECUTION_STATE_FAILED

from TIPCommon.extraction import extract_configuration_param, extract_action_param

from constants import (
    ADD_INCIDENT_COMMENT_FILE_SCRIPT_NAME,
    API_ROOT_DEFAULT,
    INTEGRATION_NAME,
)
from CrowdStrikeManager import CrowdStrikeManager


@output_handler
def main() -> None:
    siemplify = SiemplifyAction()
    siemplify.script_name = ADD_INCIDENT_COMMENT_FILE_SCRIPT_NAME

    siemplify.LOGGER.info(f"-----------Main - Param Init ---------")

    api_root = extract_configuration_param(
        siemplify,
        provider_name=INTEGRATION_NAME,
        param_name="API Root",
        is_mandatory=True,
        print_value=True,
        default_value=API_ROOT_DEFAULT,
    )
    client_id = extract_configuration_param(
        siemplify,
        provider_name=INTEGRATION_NAME,
        param_name="Client API ID",
        is_mandatory=True,
        print_value=True,
    )
    client_secret = extract_configuration_param(
        siemplify,
        provider_name=INTEGRATION_NAME,
        param_name="Client API Secret",
        is_mandatory=True,
        remove_whitespaces=False,
    )
    verify_ssl = extract_configuration_param(
        siemplify,
        provider_name=INTEGRATION_NAME,
        param_name="Verify SSL",
        input_type=bool,
        is_mandatory=True,
        print_value=True,
    )
    customer_id = extract_configuration_param(
        siemplify,
        provider_name=INTEGRATION_NAME,
        param_name="Customer ID",
        print_value=True,
    )
    incident_id = extract_action_param(
        siemplify,
        param_name="Incident ID",
        is_mandatory=True,
        print_value=True
    )
    comment = extract_action_param(
        siemplify,
        param_name="Comment",
        is_mandatory=True,
        print_value=True
    )

    siemplify.LOGGER.info("----------------- Main - Started ---------------")
    result_value = True
    status = EXECUTION_STATE_COMPLETED

    try:
        manager = CrowdStrikeManager(
            client_id=client_id,
            client_secret=client_secret,
            use_ssl=verify_ssl,
            api_root=api_root,
            logger=siemplify.LOGGER,
            customer_id=customer_id,
        )

        manager.add_incident_comment(comment, incident_id)

        output_message = (
            f"Successfully added comment to the incident {incident_id}"
            " in Crowdstrike."
        )

    except Exception as e:
        output_message = (
            "Error executing action "
            f"'{ADD_INCIDENT_COMMENT_FILE_SCRIPT_NAME}'. Reason: {e}"
        )
        status = EXECUTION_STATE_FAILED
        result_value = False
        siemplify.LOGGER.error(output_message)
        siemplify.LOGGER.exception(e)

    siemplify.end(output_message, result_value, status)
    siemplify.LOGGER.info("------------- Main - Finished -------------")


if __name__ == "__main__":
    main()
