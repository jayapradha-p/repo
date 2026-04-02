from __future__ import annotations

from dataclasses import dataclass
from io import StringIO
import json
import sys
import collections
from datetime import datetime, timedelta
from exchangelib import DELEGATE
import pytz

from SiemplifyUtils import output_handler, utc_now
from SiemplifyAction import SiemplifyAction
from SiemplifyLogger import SiemplifyLogger
from ScriptResult import (
    EXECUTION_STATE_COMPLETED,
    EXECUTION_STATE_FAILED,
    EXECUTION_STATE_INPROGRESS,
)
from TIPCommon.transformation import convert_comma_separated_to_list
from constants import (
    INTEGRATION_NAME,
    MOVE_MAIL_TO_FOLDER_SCRIPT_NAME,
    PARAMETERS_DEFAULT_DELIMITER,
    MAILBOX_DEFAULT_LIMIT,
)
from exceptions import (
    ActionFieldError,
    MailboxNotFoundError,
    NotFoundEmailsException,
    ExchangeManagerError,
    SMIMEMailError
)

from ExchangeActions import extract_action_parameter, init_manager
from ExchangeCommon import ExchangeCommon
from ExchangeManager import ExchangeManager

# maximum retry count in case of network error
MAX_RETRY = 5
LIMIT_JSON_RESULT_DEFAULT_VALUE = True
DISABLE_JSON_RESULT_DEFAULT_VALUE = False

MailboxesTuple = collections.namedtuple(
    "MailboxesTuple", ["not_processed_mailboxes", "dst_mailbox"]
)
MoveMailDetailsTuple = collections.namedtuple(
    "MoveMailDetailsTuple", ["successful_messages", "failed_mailboxes", "error_message"]
)


@dataclass
class FirstRunData:
    not_processed_mailboxes: list[str]
    dst_mailbox: str
    processed_mailboxes: list[str]
    successful_messages: list[str]
    failed_mailboxes: list[str]
    raise_mailbox_not_found_error: bool


def get_mailboxes_by_access_type(
    em: ExchangeManager,
    src_mailboxes: list[str],
    dst_mailbox: str,
    move_in_all_mailboxes: bool,
) -> MailboxesTuple:
    """
    Get mailboxes as per access type:

    Args:
      em: {ExchangeManager} The exchange manager
      src_mailboxes: {list} List of mailbox addresses to move the mail from
      dst_mailbox: {str} Destination mailbox name to move mail to
      move_in_all_mailboxes: {bool} Move in all mailboxes checkbox value

    Returns:
      MailboxesTuple:
        Named tuple of not_processed_mailboxes: list[str], dst_mailbox: str
    """
    if em.access_type == DELEGATE:
        if not dst_mailbox or not src_mailboxes:
            addresses = em.get_searchable_mailboxes_addresses(move_in_all_mailboxes)
            if not dst_mailbox:
                dst_mailbox = addresses[0]
            if not src_mailboxes:
                src_mailboxes = addresses
        return MailboxesTuple(src_mailboxes, dst_mailbox)

    if not dst_mailbox:
        dst_mailbox = em.account.primary_smtp_address

    if not src_mailboxes:
        src_mailboxes = em.get_searchable_mailboxes_addresses(
            move_in_all_mailboxes, [em.account.primary_smtp_address]
        )

    return MailboxesTuple(src_mailboxes, dst_mailbox)


def validate_mailboxes(
    em: ExchangeManager,
    src_folder_name: str,
    src_mailboxes: list[str],
    dst_folder_name: str,
    dst_mailbox: str,
    raise_mailbox_not_found_error: bool = False,
) -> None:
    """
    Checks all mailboxes validity before proceeding to move emails

    Args:
      em: {ExchangeManager} The exchange manager
      src_folder_name: {str} Source folder name, from which found emails
                        would be moved to the target folder
      src_mailboxes: {list} List of mailbox addresses to move the mail from
      dst_folder_name: {str} Destination folder name, where target emails
                            would be moved
      dst_mailbox: {str} Destination mailbox name to move mail to

    Raises:
      MailboxNotFoundError: if mailbox is not found
    """
    for src_mailbox in src_mailboxes:
        src_account = em.account
        if src_mailbox != em.account.primary_smtp_address:
            src_account = em.create_account_obj(
                src_mailbox, em.config, access_type=em.access_type
            )

        em.get_folder_object_by_name(
            folder_name=src_folder_name,
            account=src_account,
            raise_mailbox_not_found_error=raise_mailbox_not_found_error,
        )

    if dst_mailbox:
        dst_account = em.account
        if dst_mailbox == em.account.primary_smtp_address:
            dst_account = em.create_account_obj(
                dst_mailbox, em.config, access_type=em.access_type
            )

        em.get_folder_object_by_name(
            folder_name=dst_folder_name,
            account=dst_account,
            raise_mailbox_not_found_error=raise_mailbox_not_found_error,
        )


def get_action_err_msg(
    em: ExchangeManager,
    src_folder_name: str,
    dst_folder_name: str,
    src_mailbox: str,
    dst_mailbox: str,
    error: str,
) -> str:
    """
    Get action error messages

    Args:
      src_folder_name: {str} Source folder name, from which found emails
                        would be moved to the target folder
      dst_folder_name: {str} Destination folder name, where target emails would be moved
      src_mailbox: {str} Source mailbox address to move the mail from
      dst_mailbox: {str} Destination mailbox name to move mail to

    Returns:
      {str} Action specific error message
    """
    error_message = StringIO()
    if src_folder_name in error and dst_mailbox not in error:
        src_folder_err_msg = (
            "Source folder not found: "
            f"Failed to find folder {src_folder_name} "
            f"in the mailbox {src_mailbox}. "
            "Please check the spelling and "
            f"if permissions to access {src_mailbox} with "
            f"{em.access_type} access type were provisioned."
        )
        if error_message.tell() > 0:
            error_message.write("\n")
        error_message.write(src_folder_err_msg)

    if dst_folder_name in error and dst_mailbox in error:
        dst_folder_err_msg = (
            "Destination folder not found: "
            f"Failed to find folder {dst_folder_name} "
            f"in the mailbox {dst_mailbox}. "
            "Please check the spelling and "
            f"if permissions to access {src_mailbox} with "
            f"{em.access_type} access type were provisioned."
        )
        if error_message.tell() > 0:
            error_message.write("\n")
        error_message.write(dst_folder_err_msg)

    return error_message.getvalue() if error_message.getvalue() else error


def move_mail(
    em: ExchangeManager,
    logger: SiemplifyLogger,
    src_folder_name: str,
    dst_folder_name: str,
    dst_mailbox: str,
    subject_filter: str,
    only_unread: bool,
    time_filter: datetime,
    mailboxes: list[str] | None = None,
    message_ids: list[str] | None = None,
    raise_error: bool = False,
) -> MoveMailDetailsTuple:
    """
    Move mail

    Args:
      em: {ExchangeManager} The exchange manager
      logger: {SiemplifyLogger} Logger
      mailboxes: {list} List of mailbox addresses to move the mail from
      dst_folder_name: {str} Destination folder name, where target emails
                            would be moved
      src_folder_name: {str} Source folder name, from which found emails
                            would be moved to the target folder
      dst_mailbox: {str} Destination mailbox name to move mail to
      subject_filter: {str} Subject to filter emails by
      message_ids: {str} The ids of the messages to move
      only_unread: {bool} True if only unread, False otherwise.
      time_filter: {datetime} Filter by time
      raise_error: {bool}  if True raise MailboxNotFoundError
                                        else log warning for skipping mail

    Returns:
      MoveMailDetailsTuple:
        NamedTuple containing List of MessageData objects, failed mailboxes, and
        error message
    """
    failed_mailboxes = []
    successful_messages = []

    error_message = StringIO()

    for mailbox in mailboxes:
        try:
            logger.info(f"Moving messages from mailbox {mailbox}")

            if message_ids:
                for message_id in message_ids:
                    try:
                        messages = em.move_mail_from_mailbox(
                            dst_folder_name=dst_folder_name,
                            src_folder_name=src_folder_name,
                            message_id=message_id,
                            only_unread=only_unread,
                            raise_mailbox_not_found_error=raise_error,
                            subject_filter=subject_filter,
                            mailbox_address=mailbox,
                            time_filter=time_filter,
                            dst_mailbox=dst_mailbox,
                        )
                        successful_messages.extend(messages)

                    except MailboxNotFoundError:
                        raise

                    except ExchangeManagerError as e:
                        logger.error(str(e))
                        logger.exception(e)
                        error_message.write(
                            get_action_err_msg(
                                em=em,
                                src_folder_name=src_folder_name,
                                dst_folder_name=dst_folder_name,
                                src_mailbox=mailbox,
                                dst_mailbox=dst_mailbox,
                                error=str(e),
                            )
                        )
                    except SMIMEMailError as e:
                        logger.error(str(e))
                        logger.exception(e)
                        error_message.write(
                            get_action_err_msg(
                                em=em,
                                src_folder_name=src_folder_name,
                                dst_folder_name=dst_folder_name,
                                src_mailbox=mailbox,
                                dst_mailbox=dst_mailbox,
                                error=str(e),
                            )
                        )

                    except Exception as e:
                        logger.error(f"Failed to move messages from mailbox {mailbox}.")
                        logger.exception(e)
                        failed_mailboxes.append(mailbox)

            else:
                successful_messages.extend(
                    em.move_mail_from_mailbox(
                        dst_folder_name=dst_folder_name,
                        src_folder_name=src_folder_name,
                        only_unread=only_unread,
                        raise_mailbox_not_found_error=raise_error,
                        subject_filter=subject_filter,
                        mailbox_address=mailbox,
                        time_filter=time_filter,
                        dst_mailbox=dst_mailbox,
                    )
                )

        except MailboxNotFoundError:
            raise

        except ExchangeManagerError as e:
            logger.error(str(e))
            logger.exception(e)
            error_message.write(
                get_action_err_msg(
                    em=em,
                    src_folder_name=src_folder_name,
                    dst_folder_name=dst_folder_name,
                    src_mailbox=mailbox,
                    dst_mailbox=dst_mailbox,
                    error=str(e),
                )
            )
        except SMIMEMailError as e:
            logger.error(str(e))
            logger.exception(e)
            error_message.write(
                get_action_err_msg(
                    em=em,
                    src_folder_name=src_folder_name,
                    dst_folder_name=dst_folder_name,
                    src_mailbox=mailbox,
                    dst_mailbox=dst_mailbox,
                    error=str(e),
                )
            )

        except Exception as e:
            logger.error(f"Failed to move messages from mailbox {mailbox}.")
            logger.exception(e)
            failed_mailboxes.append(mailbox)

    return MoveMailDetailsTuple(
        successful_messages, list(set(failed_mailboxes)), error_message.getvalue()
    )


def execute_first_run(
    em: ExchangeManager,
    siemplify: SiemplifyAction,
    src_mailboxes: list[str],
    src_folder_name: str,
    dst_mailbox: str,
    dst_folder_name: str,
    move_in_all_mailboxes: bool,
) -> FirstRunData:
    """
    Execute First Run: execute the action flow on first run

    Args:
      em: {ExchangeManager} The exchange manager
      siemplify: {SiemplifyAction} siemplifyAction instance
      src_mailboxes: {list} List of mailbox addresses to move the mail from
      src_folder_name: {str} Source folder name, from which found emails
                        would be moved to the target folder
      dst_mailbox: {str} Destination mailbox name to move mail to
      dst_folder_name: {str} Destination folder name, where target emails
                            would be moved
      move_in_all_mailboxes: {bool} move in all mailbox

    Returns:
      FirstRunData: dataclass containing action data for further processing
    """
    if dst_mailbox and not src_mailboxes:
        raise ActionFieldError("Please provide Source Mailbox")
    if src_mailboxes and not dst_mailbox:
        raise ActionFieldError("Please provide Destination Mailbox")

    mailboxes = get_mailboxes_by_access_type(
        em=em,
        src_mailboxes=src_mailboxes,
        dst_mailbox=dst_mailbox,
        move_in_all_mailboxes=move_in_all_mailboxes,
    )
    not_processed_mailboxes = mailboxes.not_processed_mailboxes
    dst_mailbox = mailboxes.dst_mailbox

    siemplify.LOGGER.info(f"Found {len(not_processed_mailboxes)} searchable mailboxes.")
    processed_mailboxes = []
    successful_messages = []
    failed_mailboxes = []
    raise_mailbox_not_found_error = False

    if not_processed_mailboxes <= src_mailboxes:
        raise_mailbox_not_found_error = True
        siemplify.LOGGER.info("Checking if all mailboxes are valid..")
        validate_mailboxes(
            em=em,
            src_folder_name=src_folder_name,
            src_mailboxes=not_processed_mailboxes,
            dst_folder_name=dst_folder_name,
            dst_mailbox=dst_mailbox,
            raise_mailbox_not_found_error=raise_mailbox_not_found_error,
        )

    return FirstRunData(
        not_processed_mailboxes=not_processed_mailboxes,
        dst_mailbox=dst_mailbox,
        processed_mailboxes=processed_mailboxes,
        successful_messages=successful_messages,
        failed_mailboxes=failed_mailboxes,
        raise_mailbox_not_found_error=raise_mailbox_not_found_error,
    )


@output_handler
def main(is_first_run=True):
    siemplify = SiemplifyAction()
    siemplify.script_name = MOVE_MAIL_TO_FOLDER_SCRIPT_NAME
    siemplify.LOGGER.info("----------------- Main - Param Init -----------------")

    src_folder_name = extract_action_parameter(
        siemplify=siemplify, param_name="Source Folder Name", is_mandatory=True
    )
    dst_folder_name = extract_action_parameter(
        siemplify=siemplify, param_name="Destination Folder Name", is_mandatory=True
    )
    src_mailboxes = extract_action_parameter(
        siemplify=siemplify, param_name="Source Mailbox"
    )
    src_mailboxes = list(filter(None, convert_comma_separated_to_list(src_mailboxes)))
    dst_mailbox = extract_action_parameter(
        siemplify=siemplify, param_name="Destination Mailbox"
    )
    message_ids_string = extract_action_parameter(
        siemplify=siemplify, param_name="Message IDs"
    )
    subject_filter = extract_action_parameter(
        siemplify=siemplify, param_name="Subject Filter"
    )
    only_unread = extract_action_parameter(
        siemplify=siemplify,
        param_name="Only Unread",
        input_type=bool,
        default_value=False,
    )
    move_in_all_mailboxes = extract_action_parameter(
        siemplify=siemplify,
        param_name="Move in all mailboxes",
        input_type=bool,
        default_value=False,
    )
    move_in_all_mailboxes = (
        False if src_mailboxes and dst_mailbox else move_in_all_mailboxes
    )
    minutes_backwards = extract_action_parameter(
        siemplify=siemplify, param_name="Time Frame (minutes)", input_type=int
    )

    message_ids = (
        [
            mid.strip()
            for mid in message_ids_string.split(PARAMETERS_DEFAULT_DELIMITER)
            if mid and mid.strip()
        ]
        if message_ids_string
        else []
    )
    batch_size = extract_action_parameter(
        siemplify=siemplify,
        param_name="How many mailboxes to process in a single batch",
        input_type=int,
        is_mandatory=False,
        default_value=MAILBOX_DEFAULT_LIMIT,
    )
    limit_json_result = extract_action_parameter(
        siemplify=siemplify,
        input_type=bool,
        param_name="Limit the Amount of Information Returned in the JSON " "Result",
        default_value=LIMIT_JSON_RESULT_DEFAULT_VALUE,
    )

    disable_json_result = extract_action_parameter(
        siemplify=siemplify,
        input_type=bool,
        param_name="Disable the Action JSON Result",
        default_value=DISABLE_JSON_RESULT_DEFAULT_VALUE,
    )
    # Use pytz timezone object
    time_filter = (
        utc_now().replace(tzinfo=pytz.utc) - timedelta(minutes=int(minutes_backwards))
        if minutes_backwards
        else None
    )
    raise_mailbox_not_found_error = False

    siemplify.LOGGER.info("----------------- Main - Started -----------------")

    try:
        # Create new exchange manager instance
        em = init_manager(siemplify, INTEGRATION_NAME)
        if is_first_run:
            first_run_data = execute_first_run(
                em=em,
                siemplify=siemplify,
                src_mailboxes=src_mailboxes,
                src_folder_name=src_folder_name,
                dst_mailbox=dst_mailbox,
                dst_folder_name=dst_folder_name,
                move_in_all_mailboxes=move_in_all_mailboxes,
            )
            not_processed_mailboxes = first_run_data.not_processed_mailboxes
            dst_mailbox = first_run_data.dst_mailbox
            processed_mailboxes = first_run_data.processed_mailboxes
            successful_messages = first_run_data.successful_messages
            failed_mailboxes = first_run_data.failed_mailboxes
            raise_mailbox_not_found_error = first_run_data.raise_mailbox_not_found_error
        else:
            additional_data = json.loads(siemplify.parameters["additional_data"])
            successful_messages = [
                em.parser.get_message_data(message_json, False)
                for message_json in additional_data.get("successful_messages", [])
            ]
            failed_mailboxes = additional_data.get("failed_mailboxes", [])
            processed_mailboxes = additional_data.get("processed_mailboxes", [])
            not_processed_mailboxes = additional_data.get("not_processed_mailboxes", [])

        batch = not_processed_mailboxes[:batch_size]
        siemplify.LOGGER.info(f"Processing {len(batch)} mailboxes.")
        move_mail_details = move_mail(
            em=em,
            logger=siemplify.LOGGER,
            mailboxes=batch,
            src_folder_name=src_folder_name,
            dst_folder_name=dst_folder_name,
            dst_mailbox=dst_mailbox,
            subject_filter=subject_filter,
            message_ids=message_ids,
            only_unread=only_unread,
            time_filter=time_filter,
            raise_error=raise_mailbox_not_found_error,
        )
        batch_successful_messages = move_mail_details.successful_messages
        batch_failed_mailboxes = move_mail_details.failed_mailboxes
        error_message = move_mail_details.error_message

        siemplify.LOGGER.info(
            f"Moved {len(batch_successful_messages)} messages from "
            f"{len(batch) - len(batch_failed_mailboxes)} mailboxes "
            f"(out of {len(batch)} mailboxes in current batch)."
        )

        processed_mailboxes.extend(batch)
        not_processed_mailboxes = not_processed_mailboxes[batch_size:]
        failed_mailboxes.extend(batch_failed_mailboxes)
        successful_messages.extend(batch_successful_messages)

        if not not_processed_mailboxes:
            # Completed processing all mailboxes
            if not successful_messages:
                raise NotFoundEmailsException

            output_message = StringIO()
            if failed_mailboxes:
                output_message.write(
                    "Failed to access following mailboxes - "
                    f"{PARAMETERS_DEFAULT_DELIMITER.join(failed_mailboxes)}\n"
                )
                if error_message:
                    output_message.write(f"\n{error_message}")

            status = EXECUTION_STATE_COMPLETED
            result_value = True

            if not limit_json_result:
                json_result = json.dumps(
                    [message.to_json() for message in successful_messages]
                )
            else:
                json_result = json.dumps(
                    [message.to_shorthand_json() for message in successful_messages]
                )
            if not disable_json_result:
                siemplify.result.add_result_json(json_result)
            if message_ids:
                output_message.write(
                    f"Successfully moved {len(successful_messages)} out of "
                    f"{len(message_ids)} found emails "
                    f"from {src_folder_name} to {dst_folder_name}"
                )
            else:
                output_message.write(
                    f"{len(successful_messages)} mails were successfully "
                    f"moved from {src_folder_name} to {dst_folder_name}"
                )
            if error_message:
                output_message.write(f"\n{error_message}")
            output_message = output_message.getvalue()

        else:
            # There are still mailboxes to process
            additional_data = {
                "successful_messages": [
                    message.to_json() for message in successful_messages
                ],
                "failed_mailboxes": failed_mailboxes,
                "not_processed_mailboxes": not_processed_mailboxes,
                "processed_mailboxes": processed_mailboxes,
            }
            output_message = (
                f"{len(successful_messages)} email(s) were found in "
                f"{len(processed_mailboxes)} mailboxes (out "
                f"of {len(processed_mailboxes) + len(not_processed_mailboxes)}). "
                "Continuing."
            )
            status = EXECUTION_STATE_INPROGRESS
            result_value = json.dumps(additional_data)

    except MailboxNotFoundError as e:
        output_message = (
            "Error running action as the source mailbox " f"{str(e)} was not found!"
        )
        if dst_mailbox == str(e):
            output_message = (
                "Error running action as the destination mailbox "
                f"{dst_mailbox} was not found!"
            )
        siemplify.LOGGER.error(output_message)
        siemplify.LOGGER.exception(e)
        result_value = False
        status = EXECUTION_STATE_FAILED

    except SMIMEMailError:
        result_value = False
        output_message = "No mails were found matching the search criteria!"
        if error_message:
            output_message += f"\n{error_message}"
        status = EXECUTION_STATE_COMPLETED

    except NotFoundEmailsException:
        result_value = False
        output_message = "No mails were found matching the search criteria!"
        if error_message:
            output_message += f"\n{error_message}"
        status = EXECUTION_STATE_COMPLETED

    except Exception as e:
        siemplify.LOGGER.error(
            f"General error performing action {MOVE_MAIL_TO_FOLDER_SCRIPT_NAME}"
        )
        siemplify.LOGGER.exception(e)
        status = EXECUTION_STATE_FAILED
        result_value = False
        output_message = f"Error: {e}"
        additional_data_json = extract_action_parameter(
            siemplify=siemplify, param_name="additional_data", default_value="{}"
        )
        output_message, result_value, status = (
            ExchangeCommon.prevent_async_action_fail_in_case_of_network_error(
                e, additional_data_json, MAX_RETRY, output_message, result_value, status
            )
        )

    siemplify.LOGGER.info("----------------- Main - Finished -----------------")
    siemplify.LOGGER.info(f"Status: {status}")
    siemplify.LOGGER.info(f"Result Value: {result_value}")
    siemplify.LOGGER.info(f"Output Message: {output_message}")

    siemplify.end(output_message, result_value, status)


if __name__ == "__main__":
    is_first_run = len(sys.argv) < 3 or sys.argv[2] == "True"
    main(is_first_run)
