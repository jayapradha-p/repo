from SiemplifyAction import SiemplifyAction
from SiemplifyUtils import output_handler
from ExchangeActions import extract_action_parameter, init_manager
from ScriptResult import EXECUTION_STATE_COMPLETED, EXECUTION_STATE_FAILED
from constants import (
    INTEGRATION_NAME,
    SAVE_MAIL_ATTACHMENTS_TO_THE_CASE_SCRIPT_NAME,
    PARAMETERS_DEFAULT_DELIMITER,
)
from exceptions import (
    NotFoundAttachmentsException,
    NotFoundEmailsException,
    SMIMEMailError
)

@output_handler
def main():
    siemplify = SiemplifyAction()
    siemplify.script_name = SAVE_MAIL_ATTACHMENTS_TO_THE_CASE_SCRIPT_NAME
    siemplify.LOGGER.info("----------------- Main - Param Init -----------------")

    folders_string = extract_action_parameter(
        siemplify=siemplify, param_name="Folder Name", is_mandatory=True
    )
    message_id = extract_action_parameter(
        siemplify=siemplify, param_name="Message ID", is_mandatory=True
    )
    attachment_name = extract_action_parameter(
        siemplify=siemplify, param_name="Attachment To Save"
    )

    folders_names = (
        [
            f.strip()
            for f in folders_string.split(PARAMETERS_DEFAULT_DELIMITER)
            if f.strip()
        ]
        if folders_string
        else []
    )

    siemplify.LOGGER.info("----------------- Main - Started -----------------")
    saved_attachments = []
    result_value = False
    status = EXECUTION_STATE_COMPLETED
    output_message = ""

    try:
        em = init_manager(siemplify, INTEGRATION_NAME)
        em.enable_support_all_attachment_types()
        message = None
        smime_errors = []
        for folder in folders_names:
            try:
                filtered_messages = em.get_messages_data(
                    message_id=message_id, folder_name=folder
                ).results
                if filtered_messages:
                    # since we are fetching by message_id we should get only first (and only?) one
                    message = filtered_messages[0]
            except SMIMEMailError as e:
                siemplify.LOGGER.error(
                    f"Failed to get email from folder={folder} "
                    f"with message_id={message_id}"
                )
                siemplify.LOGGER.exception(e)
                smime_errors.append(str(e))
            except Exception as e:
                siemplify.LOGGER.error(
                    f"Failed to get email from folder={folder} "
                    f"with message_id={message_id}"
                )
                siemplify.LOGGER.exception(e)

        if not message:
            if smime_errors:
                raise SMIMEMailError(smime_errors[0])
            raise NotFoundEmailsException

        attachments = message.attachments_list

        # Filters attachments list by a specific attachment(s) name if filter value exist
        if attachment_name:
            attachments = {
                filename: content
                for filename, content in attachments.items()
                if filename == attachment_name
            }

        if not attachments:
            raise NotFoundAttachmentsException

        try:
            for filename, content in attachments.items():
                siemplify.result.add_attachment(
                    title=message_id, filename=filename, file_contents=content
                )
                saved_attachments.append(filename)

        except Exception as e:
            siemplify.LOGGER.exception(e)

        if saved_attachments:
            siemplify.result.add_result_json(message.to_json())
            output_message = (
                "Successfully saved the following attachments from the email "
                f"{message_id}: {PARAMETERS_DEFAULT_DELIMITER.join(saved_attachments)}")
            result_value = True

    except NotFoundEmailsException:
        output_message = "No email was found"
    except SMIMEMailError as e:
        output_message = f"No email was found: {str(e)}"
    except NotFoundAttachmentsException:
        output_message = f"No attachments found in email {message_id}"
    except Exception as e:
        siemplify.LOGGER.error(
            "General error performing action "
            f"{SAVE_MAIL_ATTACHMENTS_TO_THE_CASE_SCRIPT_NAME}"
        )
        siemplify.LOGGER.exception(e)
        status = EXECUTION_STATE_FAILED
        output_message = (
            f"Failed to save the email attachments to the case, the error is: {e}"
        )

    siemplify.LOGGER.info("----------------- Main - Finished -----------------")
    siemplify.LOGGER.info(f"Status: {status}")
    siemplify.LOGGER.info(f"Result Value: {result_value}")
    siemplify.LOGGER.info(f"Output Message: {output_message}")

    siemplify.end(output_message, result_value, status)


if __name__ == "__main__":
    main()
