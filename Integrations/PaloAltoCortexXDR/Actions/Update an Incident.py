from exceptions import XDRMissingParametersException
from SiemplifyAction import SiemplifyAction
from ScriptResult import EXECUTION_STATE_FAILED, EXECUTION_STATE_COMPLETED

from action_init import create_api_client
from constants import INTEGRATION_NAME, UPDATE_INCIDENT_ACTION_SCRIPT_NAME


ID_NOT_FOUND = "incident not found"
SELECT_ONE = "Select One"


def main():
    # Configuration.
    siemplify = SiemplifyAction()
    siemplify.script_name = UPDATE_INCIDENT_ACTION_SCRIPT_NAME

    siemplify.LOGGER.info("================= Main - Param Init =================")
    incident_id = siemplify.parameters.get("Incident ID")
    assigned_user = siemplify.parameters.get("Assigned User Name")
    severity = siemplify.parameters.get("Severity")
    incident_status = siemplify.parameters.get("Status")

    siemplify.LOGGER.info("----------------- Main - Started -----------------")
    xdr_manager = create_api_client(siemplify)
    err_msg_prefix = (
        f"Error executing action {UPDATE_INCIDENT_ACTION_SCRIPT_NAME}. Reason:"
    )

    try:
        if not assigned_user and incident_status == severity == SELECT_ONE:
            raise XDRMissingParametersException(
                'At least of the "Assigned User Name", "Severity" or "Status"'
                "parameters should have a provided value."
            )
        xdr_manager.update_an_incident(
            incident_id,
            assigned_user=assigned_user,
            severity=None if severity == SELECT_ONE else severity,
            status=None if incident_status == SELECT_ONE else incident_status,
        )
        output_message = (
            "Successfully updated one or more fields of incident with ID: "
            f"{incident_id}"
        )
        result_value = "true"
        status = EXECUTION_STATE_COMPLETED
    except XDRMissingParametersException as e:
        siemplify.LOGGER.error(e)
        output_message = f"{err_msg_prefix} {e}"
        result_value = "false"
        status = EXECUTION_STATE_FAILED
    except Exception as e:
        error_string = str(e).lower()
        if ID_NOT_FOUND in error_string:
            output_message = (
                f"{err_msg_prefix} incidents with ID {incident_id} wasn't found in "
                f"{INTEGRATION_NAME}, please check the spelling."
            )
        else:
            siemplify.LOGGER.error(f"Failed to update incident: {incident_id}")
            siemplify.LOGGER.exception(e)
            output_message = f"{err_msg_prefix} {e}"
        result_value = "false"
        status = EXECUTION_STATE_FAILED
    siemplify.LOGGER.info("----------------- Main - Finished -----------------")
    siemplify.LOGGER.info(
        f"\n  result_value: {result_value}\n  output_message: {output_message}"
    )
    siemplify.end(output_message, result_value, status)


if __name__ == "__main__":
    main()
