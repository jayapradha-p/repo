from SiemplifyAction import SiemplifyAction

from action_init import create_api_client
from constants import PING_ACTION_SCRIPT_NAME


def main():
    siemplify = SiemplifyAction()
    siemplify.script_name = PING_ACTION_SCRIPT_NAME
    siemplify.LOGGER.info("================= Main - Param Init =================")
    siemplify.LOGGER.info("----------------- Main - Started -----------------")
    create_api_client(siemplify)

    output_message = "Successfully connected to Palo Alto Cortex XDR"
    result_value = "true"

    siemplify.LOGGER.info("----------------- Main - Finished -----------------")
    siemplify.LOGGER.info(
        f"\n  result_value: {result_value}\n  output_message: {output_message}"
    )
    siemplify.end(output_message, result_value)


if __name__ == "__main__":
    main()
