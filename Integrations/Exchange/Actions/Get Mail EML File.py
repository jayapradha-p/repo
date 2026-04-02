from SiemplifyUtils import output_handler
from SiemplifyAction import SiemplifyAction
from ExchangeActions import extract_action_parameter, init_manager
from ScriptResult import EXECUTION_STATE_COMPLETED, EXECUTION_STATE_FAILED
from constants import INTEGRATION_NAME, GET_MAIL_EML_FILE_SCRIPT_NAME

EML_FILE_NAME_PATTERN = "{}.eml"  # {} - Mail ID.


@output_handler
def main():
    siemplify = SiemplifyAction()
    siemplify.script_name = GET_MAIL_EML_FILE_SCRIPT_NAME
    status = EXECUTION_STATE_COMPLETED
    result_value = ""

    siemplify.LOGGER.info("----------------- Main - Param Init -----------------")

    # Parameters.
    message_id = extract_action_parameter(
        siemplify=siemplify, param_name="Message ID", is_mandatory=True
    )
    is_result_value_base64 = extract_action_parameter(
        siemplify=siemplify,
        param_name="Base64 Encode",
        input_type=bool,
        default_value=True,
    )
    folder_name = extract_action_parameter(
        siemplify=siemplify, param_name="Folder Name", default_value="Inbox"
    )

    siemplify.LOGGER.info("----------------- Main - Started -----------------")

    try:
        # Create new exchange manager instance
        em = init_manager(siemplify, INTEGRATION_NAME)

        messages = em.receive_mail(message_id=message_id, folder_name=folder_name)

        if messages:
            message = em.set_extracted_data_to_smime_message(messages[0])
            eml = em.get_mail_mime_content(message)
            eml_base64 = em.get_mail_mime_content(message, base64_encode=True)

            # Add EML as attachment
            siemplify.result.add_attachment(
                message_id, EML_FILE_NAME_PATTERN.format(message_id), eml_base64
            )

            output_message = f"Fetched EML data for message with ID: {message_id}."
            result_value = eml_base64 if is_result_value_base64 else eml
        else:
            output_message = f"No EML data was fetched for mail with ID: {message_id}"

    except Exception as e:
        siemplify.LOGGER.error(
            f"General error performing action {GET_MAIL_EML_FILE_SCRIPT_NAME}"
        )
        siemplify.LOGGER.exception(e)
        status = EXECUTION_STATE_FAILED
        output_message = f"An error occurred while running action: {e}"

    siemplify.LOGGER.info("----------------- Main - Finished -----------------")
    siemplify.LOGGER.info(f"Status: {status}")
    siemplify.LOGGER.info(f"Result Value: {result_value}")
    siemplify.LOGGER.info(f"Output Message: {output_message}")

    siemplify.end(output_message, result_value, status)


if __name__ == "__main__":
    main()
