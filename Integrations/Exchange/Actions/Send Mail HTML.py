from ExchangeActions import extract_action_parameter, init_manager
from ScriptResult import EXECUTION_STATE_COMPLETED, EXECUTION_STATE_FAILED
from SiemplifyUtils import output_handler
from SiemplifyAction import SiemplifyAction
from constants import (
    INTEGRATION_NAME,
    MAX_SUBJECT_LENGTH,
    PARAMETERS_DEFAULT_DELIMITER,
    SEND_MAIL_HTML_SCRIPT_NAME,
)


@output_handler
def main():
    siemplify = SiemplifyAction()
    siemplify.script_name = SEND_MAIL_HTML_SCRIPT_NAME
    siemplify.LOGGER.info("----------------- Main - Param Init -----------------")

    output_message = "Mail sent successfully"
    result_value = True
    status = EXECUTION_STATE_COMPLETED

    send_to = extract_action_parameter(
        siemplify=siemplify, param_name="Send to", is_mandatory=True
    )
    subject = extract_action_parameter(
        siemplify=siemplify, param_name="Subject", is_mandatory=True
    )
    content = extract_action_parameter(
        siemplify=siemplify, param_name="Mail content", is_mandatory=True
    )
    cc = extract_action_parameter(siemplify=siemplify, param_name="CC")
    bcc = extract_action_parameter(siemplify=siemplify, param_name="BCC")
    attachment_paths_string = extract_action_parameter(
        siemplify=siemplify, param_name="Attachments Paths"
    )

    attachment_paths = (
        [
            a.strip()
            for a in attachment_paths_string.split(PARAMETERS_DEFAULT_DELIMITER)
            if a.strip()
        ]
        if attachment_paths_string
        else []
    )

    if len(subject) > MAX_SUBJECT_LENGTH:
        subject = subject[:MAX_SUBJECT_LENGTH]
        siemplify.LOGGER.info(
            "The subject length exceeds the maximum allowed length(255) "
            "trimming it to fit within the limit."
        )
        siemplify.LOGGER.info(f"Trimmed subject: {subject}")

    siemplify.LOGGER.info("----------------- Main - Started -----------------")

    try:
        # Create new exchange manager instance
        em = init_manager(siemplify, INTEGRATION_NAME)
        generate_mail_id = em.is_writable_mail_id_supported()

        em.send_mail_html_embedded_photos(
            to_addresses=send_to,
            subject=subject,
            html_body=content,
            attachments_paths=attachment_paths,
            cc=cc,
            bcc=bcc,
            generate_mail_id=generate_mail_id,
        )
    except Exception as e:
        siemplify.LOGGER.error(
            f"General error performing action {SEND_MAIL_HTML_SCRIPT_NAME}"
        )
        siemplify.LOGGER.exception(e)
        status = EXECUTION_STATE_FAILED
        result_value = False
        output_message = f"An error occurred while running action: {e}"

    siemplify.LOGGER.info("----------------- Main - Finished -----------------")
    siemplify.LOGGER.info(f"Status: {status}")
    siemplify.LOGGER.info(f"Result Value: {result_value}")
    siemplify.LOGGER.info(f"Output Message: {output_message}")

    siemplify.end(output_message, result_value, status)


if __name__ == "__main__":
    main()
