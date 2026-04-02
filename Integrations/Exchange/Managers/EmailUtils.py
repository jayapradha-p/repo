# =====================================
#              IMPORTS                #
# =====================================
from __future__ import annotations
import base64
import copy
import email
import email.header
import hashlib
import itertools
import os
import re
import time
from base64 import b64decode, b64encode
from copy import deepcopy
from datetime import datetime
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from io import BytesIO
import subprocess

import compressed_rtf
import extract_msg
import html2text
from asn1crypto import x509
from emaildata.metadata import MetaData, text_to_utf8
from icalendar import Calendar
from oscrypto import asymmetric
from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.xhtml.writer import XHTMLWriter
from smail.sign import (
    DeprecatedDigestError,
    UnsupportedDigestError,
    UnsupportedSignatureError,
)
from smail.signer import sign_bytes
from smail.utils import MAC_NEWLINE, UNIX_NEWLINE, WINDOWS_NEWLINE
from exchangelib import FileAttachment

from SiemplifyConnectorsDataModel import CaseInfo
from TIPCommon.types import SingleJson

from ExchangeUtilsManager import decode_url, save_content_to_file, flat_dict_to_list
from ExchangeInboxRules import UpdateInboxRules
from exceptions import FileError, SMIMEMailError
from constants import (
    CHARS_TO_STRIP,
    DEFAULT_URLS_LIST_DELIMITER,
    PARAMETERS_DEFAULT_DELIMITER,
    SmimeType,
    URLS_REGEX,
    URLS_REGEX_COMPLEX,
    URL_ENCLOSING_PREFIX,
    URL_ENCLOSING_SUFFIX,
)


# =====================================
#             CONSTANTS               #
# =====================================

ENCODING_MAPPING = {"iso-8859-8-i": "iso-8859-8"}
ANSWER_PLACEHOLDER_PATTERN = "(?<={{)[^{]*(?=}})"
DATA_ATTACHMENT = "data"
INNER_MSG_NOT_SUPPORTED = "Inner .msg attachment is present but not supported."

MAIL_SUBJECT_KEY = "subject"

EMAIL_PREFIX = "mailto:"
MESSAGE_ID_FORMAT = "<{}>"
DEFAULT_DIVIDER = ";"
DEFAULT_URLS_DIVIDER = "|"

SIEMPLIFY_MAIL_DICT_HTML_BODY_KEY = "html_body"
SIEMPLIFY_MAIL_DICT_PLAINTEXT_BODY_KEY = "plaintext_body"
SIEMPLIFY_MAIL_DICT_RESOLVED_BODY_KEY = "body"
SIEMPLIFY_MAIL_DICT_TO_KEY = "to"
SIEMPLIFY_MAIL_DICT_CC_KEY = "cc"
SIEMPLIFY_MAIL_DICT_BCC_KEY = "bcc"
SIEMPLIFY_MAIL_DICT_SENDER_KEY = "sender"
SIEMPLIFY_MAIL_DICT_SUBJECT_KEY = "subject"
SIEMPLIFY_MAIL_DICT_MESSAGE_ID_KEY = "message_id"
SIEMPLIFY_MAIL_DICT_RECEIVERS_KEY = "receivers"
SIEMPLIFY_MAIL_DICT_REPLY_TO_KEY = "reply_to"
SIEMPLIFY_MAIL_DICT_IN_REPLY_TO_KEY = "in_reply_to"
SIEMPLIFY_MAIL_DICT_RAW_EML_KEY = "raw"
SIEMPLIFY_MAIL_DICT_DATE_KEY = "date"
SIEMPLIFY_MAIL_DICT_TIMESTAMP_KEY = "timestamp"
SIEMPLIFY_MAIL_DICT_UNIXTIME_DATE_KEY = "unixtime_date"
SIEMPLIFY_MAIL_DICT_EMAIL_ID_KEY = "email_uid"
SIEMPLIFY_MAIL_DICT_ANSWER_ID_KEY = "answer"
SIEMPLIFY_MAIL_DICT_NAMES_KEY = "names"
SIEMPLIFY_MAIL_DICT_DISPLAY_NAME_KEY = "display_name"


# We have email validator in SiemplifyUtils.py
# but regex in it is not compatible with emails we have
# for testing example: john_doe@siemplifylab.local
# and that's why I have used this regex.
VALID_EMAIL_REGEXP = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"


# =====================================
#              CLASSES                #
# =====================================


def remove_fields_from_case_events(case: CaseInfo, fields_to_remove: list[str]) -> None:
    for event in case.events:
        for field in fields_to_remove:
            event.pop(field, None)


def is_valid_email(user_name):
    """
    Check if the user_name is valid email.
    :param user_name: {str} User name
    :return: {bool} True if valid email, else False
    """
    return bool(re.search(VALID_EMAIL_REGEXP, user_name))


def message_as_string(msg, logger=None):
    # Work around for https://bugs.python.org/issue27321
    try:
        value = email.message.Message.as_string(msg)
    except (KeyError, LookupError, UnicodeEncodeError) as e:
        if logger is not None:
            logger.info(
                f"Failed to flatten message as string with an error: {e}. "
                "Falling back to flatten message as bytes and then decode"
            )
        value = email.message.Message.as_bytes(msg).decode("ascii", "replace")
    return value


def get_charset(message, default_charset="utf-8"):
    """
    Get the message charset
    :param message: {email.message.Message} An eml object
    :param default_charset: {str} Default charset, which should be used
    :return: {str} Charset name
    """
    try:
        charset = message.get_content_charset()
        if not charset:
            charset = message.get_charset()

        if charset:
            if charset.find('"') > 0:
                charset = charset[: charset.find('"')]
            if charset == "iso-8859-8-i":
                charset = "iso-8859-8"
            return charset
    except:
        pass
    return default_charset


def decode_header_value(header_value):
    """
    Extract message header value from email message.
    :param header_value: {str} The raw header value.
    :return: {unicode} The parsed header value.
    """
    if not header_value:
        return ""

    try:
        parsed_value, encoding = email.header.decode_header(header_value)[0]
        if isinstance(parsed_value, str):
            return parsed_value

        if not encoding:
            return parsed_value.decode("utf-8")

        return parsed_value.decode(encoding)

    except Exception as e:
        try:
            # Workaround for the wrong encoding sometimes used with a Chinese text, if parser fails to decode the text
            # we will try to use standard Chinese codec instead and only then fallback to utf-8
            return text_to_utf8(parsed_value, enc="gb18030")
        except UnicodeDecodeError:
            try:
                return parsed_value.decode()
            except UnicodeDecodeError:
                return "Unable to decode email subject"

        return str(e)


def get_html_urls(html_content):
    """
    Get urls from html content
    :param html_content: {str} The html content
    :return: {tuple} Comma-separated list of visible urls, comma-separated list of not visible urls from original src attribute
    """
    regex_object = re.compile(URLS_REGEX_COMPLEX)
    urls_list, original_src_urls_list = get_html_urls_from_html_2_text_obj(html_content)

    urls_list = list(
        set(
            [
                check_url_enclosing(decode_url(regex_object.search(url).group(0)))
                for url in urls_list
                if regex_object.search(url)
            ]
        )
    )
    original_src_urls_list = list(
        set(
            [
                check_url_enclosing(decode_url(regex_object.search(url).group(0)))
                for url in original_src_urls_list
                if regex_object.search(url)
            ]
        )
    )

    return DEFAULT_URLS_DIVIDER.join(urls_list), DEFAULT_URLS_DIVIDER.join(
        original_src_urls_list
    )


def check_url_enclosing(url):
    """
    Check if url enclosed and remove enclosing characters
    :param url: {str} url to check
    :return: {str} transformed url
    """
    if url.startswith(URL_ENCLOSING_PREFIX) and url.endswith(URL_ENCLOSING_SUFFIX):
        return url[1:-1]

    return url


def get_html_urls_from_html_2_text_obj(html_content):
    """
    Create a HTML2Text object and get html urls
    :param html_content: {str} The html content
    :return: {tuple} The list of visible urls, the list of not visible urls from original src attribute
    """
    html_renderer = html2text.HTML2Text()
    html_renderer.ignore_tables = True
    html_renderer.protect_links = True
    html_renderer.ignore_images = False
    html_renderer.ignore_links = False
    html_renderer.handle(html_content)
    return html_renderer.html_links, html_renderer.html_links_original_src


def get_unicode_str(value):
    """
    Checks type of the string and if it's a binary string, then decodes it to unicode
    :param value: {object} string or binary string
    :return: {str} Unicode decoded string
    """

    try:
        if isinstance(value, bytes):
            return value.decode()
        return str(value)
    except Exception:
        return value


def create_message(
    recipients, subject, html_content=None, cc=None, bcc=None, attachments=None
):
    """
    Creates and returns a message object
    :param recipients: {list} List of message recipients
    :param subject: {str} The message subject
    :param html_content: {str} The HTML content of the message
    :param cc: {list} List of emails to be included to CC
    :param bcc: {list} List of emails to be included to BCC
    :param attachments: {list} A list of file path strings
    :return: {email.message.Message} Message object
    """
    msg_root = MIMEMultipart("mixed")
    msg_root["To"] = PARAMETERS_DEFAULT_DELIMITER.join(recipients)
    msg_root["Subject"] = Header(subject)

    if cc:
        msg_root["CC"] = PARAMETERS_DEFAULT_DELIMITER.join(cc)

    if bcc:
        msg_root["BCC"] = PARAMETERS_DEFAULT_DELIMITER.join(bcc)

    msg_related = MIMEMultipart("related")
    msg_root.attach(msg_related)

    msg_alternative = MIMEMultipart("alternative")
    msg_related.attach(msg_alternative)

    msg_html = MIMEText(html_content, "html")
    msg_alternative.attach(msg_html)

    if attachments:
        for attachment in attachments:
            fname = os.path.basename(attachment)

            with open(attachment, "rb") as f:
                msg_attach = MIMEBase("application", "octet-stream")
                msg_attach.set_payload(f.read())
                encoders.encode_base64(msg_attach)
                msg_attach.add_header(
                    "Content-Disposition",
                    "attachment",
                    filename=(Header(fname).encode()),
                )
                msg_attach.add_header("Content-ID", f"<{(Header(fname).encode())}>")
                msg_root.attach(msg_attach)

    return msg_root


def sign_message(
    message,
    key_signer,
    cert_signer,
    digest_alg="sha256",
    sig_alg="rsa",
    attrs=True,
    prefix="",
    allow_deprecated=False,
    include_cert_signer=True,
    additional_certs=None,
    multipart_class=MIMEMultipart,
):
    """
    Takes a message, signs it and returns a new signed message object
    :param message: {email.message.Message} Message object to sign
    :param key_signer: {bytes, str, asn1crypto.keys.PrivateKeyInfo or oscrypto.asymmetric.PrivateKey} Private key used to sign the message
    :param cert_signer: {bytes, str, asn1crypto.x509.Certificate or oscrypto.asymmetric.Certificate} Certificate/Public Key that will be included in the signed message
    :param digest_alg: {str} Digest (Hash) Algorithm - e.g. "sha256"
    :param sig_alg: {str} Signature algorithm
    :param attrs: {bool} Whether to include signed attributes (signing time)
    :param prefix: {str}: Content type prefix (e.g. "x-")
    :param allow_deprecated: {bool} Whether deprecated digest algorithms should be allowed
    :param include_cert_signer: {bool} Whether to include the public certificate of the signer in the signed data
    :param additional_certs {list} List of asn1crypto.x509.Certificate objects, additional certificates to be included (e.g. Intermediate or Root CA certs)
    :param multipart_class: {class}: Which MIMEMultiPart class should be used
    :return: {email.message.Message} Signed message
    """
    # private key
    if not isinstance(key_signer, asymmetric.PrivateKey):
        key_signer = asymmetric.load_private_key(key_signer)

    # cert
    if not isinstance(cert_signer, x509.Certificate):
        cert_signer_oscrypto = asymmetric.load_certificate(cert_signer)
        cert_signer = cert_signer_oscrypto.asn1

    if digest_alg == "md5":
        micalg = "md5"
        if allow_deprecated is False:
            raise DeprecatedDigestError(f"{digest_alg} is deprecated")
    elif digest_alg == "sha1":
        micalg = "sha-1"
        if allow_deprecated is False:
            raise DeprecatedDigestError(f"{digest_alg} is deprecated")
    elif digest_alg == "sha256":
        micalg = "sha-256"
    elif digest_alg == "sha512":
        micalg = "sha-512"
    else:
        raise UnsupportedDigestError(f"{digest_alg} is unknown or unsupported")

    if sig_alg == "rsa":
        pass
    elif sig_alg == "pss":
        pass
    else:
        raise UnsupportedSignatureError(f"{sig_alg} is unknown or unsupported")

    additional_x509 = []

    if additional_certs:
        for additional in additional_certs:
            if not isinstance(additional, x509.Certificate):
                additional_oscrypto = asymmetric.load_certificate(additional)
                additional = additional_oscrypto.asn1

            additional_x509.append(additional)

    # make a deep copy of original message to avoid any side effects (original will not be touched)
    copied_msg = deepcopy(message)

    headers = {}
    # besides some special ones (e.g. Content-Type) remove all headers before signing the body content
    for hdr_name in copied_msg.keys():
        if hdr_name in ["Content-Type", "MIME-Version", "Content-Transfer-Encoding"]:
            continue

        values = copied_msg.get_all(hdr_name)
        if values:
            del copied_msg[hdr_name]
            headers[hdr_name] = values

    data_unsigned = message_as_string(copied_msg)
    data_unsigned = data_unsigned.replace(WINDOWS_NEWLINE, UNIX_NEWLINE).replace(
        MAC_NEWLINE, UNIX_NEWLINE
    )
    data_unsigned = data_unsigned.encode()
    data_signed = sign_bytes(
        data_unsigned,
        key_signer,
        cert_signer,
        digest_alg,
        sig_alg,
        attrs=attrs,
        include_cert_signer=include_cert_signer,
        additional_certs=additional_x509,
    )
    data_signed = base64.encodebytes(data_signed)

    new_msg = multipart_class(
        "signed", protocol=f"application/{prefix}pkcs7-signature", micalg=micalg
    )
    # add original headers
    for hdr, values in headers.items():
        for val in values:
            new_msg.add_header(hdr, str(val))
    new_msg.preamble = "This is an S/MIME signed message"

    # attach original message
    new_msg.attach(copied_msg)

    msg_signature = MIMEBase(
        "application", f"{prefix}pkcs7-signature", name="smime.p7s"
    )
    msg_signature.add_header("Content-Transfer-Encoding", "base64")
    msg_signature.add_header("Content-Disposition", "attachment", filename="smime.p7s")
    msg_signature.add_header("Content-Description", "S/MIME Cryptographic Signature")
    msg_signature.__delitem__("MIME-Version")
    msg_signature.set_payload(data_signed)

    new_msg.attach(msg_signature)

    return new_msg


class EmailUtils:
    EMPTY_SUBJECT = "Empty subject"
    UNKNOWN_SENDER = "Unknown sender"

    def __init__(self, logger, urls_regex: str | None = None):
        super().__init__()
        self.logger = logger
        self.urls_regex = urls_regex

    @staticmethod
    def is_attachment(mime_part, include_inline=False):
        """
        Determine if a MIME part is a valid attachment or not.
        Based on :
        https://www.ietf.org/rfc/rfc2183.txt
        More about the content-disposition allowed fields and values:
        https://www.iana.org/assignments/cont-disp/cont-disp.xhtml#cont-disp-1
        :param mime_part: {email.message.Message} The MIME part
        :param include_inline: {bool} Whether to consider inline attachments as well or now
        :return: {bool} True if MIME part is an attachment, False otherwise
        """
        # Each attachment should have the Content-Disposition header
        content_disposition = mime_part.get("Content-Disposition")

        if not content_disposition or not isinstance(content_disposition, str):
            return False

        # "Real" attachments differs from inline attachments (like images in signature)
        # by having Content-Disposition headers, that starts with 'attachment'.
        # Inline attachments have the word 'inline' at the beginning of the header.
        # Inline attachments are being displayed as part of the email, and not as a separate
        # file. In most cases, the term attachment is related to the MIME parts that start with
        # 'attachment'.
        # The values are not case sensitive
        if content_disposition.lower().startswith("attachment"):
            return True

        if include_inline and content_disposition.lower().startswith("inline"):
            return True

        return False

    def extract_filename(self, mime_part):
        """
        Extract the filename of an attachment MIME part
        :param mime_part: {email.message.Message} The MIME part
        :return: {unicode} The decoded filename
        """
        # This is based on email.get_filename() method. The original method decodes
        # the header according to rfc2231, but its not consistent on the return value
        # (sometimes its str, if all the text is ASCII, and otherwise its unicode).
        missing = object()

        filename = mime_part.get_param("filename", missing, "content-disposition")

        if filename is missing:
            filename = mime_part.get_param("name", missing, "content-disposition")

        if filename is missing:
            return

        return decode_header_value(filename)

    def _extract_attachments_from_eml(
        self, msg, encode_as_base64=False, convert_utf8=True, exclude_attachments=None
    ):
        """
        Extract the attachments {filename: file_content} from a email.message.Message object (eml Mime).
        :param msg: {email.message.Message} the msg to extract from
        :param encode_as_base64: {bool} Whether to encode the attachments content with base64 or not
        :param convert_utf8: {bool} Whether to convert the filename to utf8
        :param exclude_attachments: {list} The list of the attachments names should be ignored
        :return: {dict} The extracted attachments (filename: content)
        """
        attachments_dict = {}

        if msg.is_multipart():
            attachments = msg.get_payload()
            index = 0

            for attachment in attachments:
                if self.is_attachment(attachment):

                    if attachment.get_content_type() == "message/rfc822":
                        # The attachment is an inner message object similar to ItemAttachment like in Outlook
                        file_content = message_as_string(
                            attachment.get_payload()[0], logger=self.logger
                        )
                        file_content_for_md5 = (
                            file_content.encode()
                            if isinstance(file_content, str)
                            else file_content
                        )
                        md5_file_hash = hashlib.md5(file_content_for_md5).hexdigest()
                        filename = self.extract_subject(
                            email.message_from_string(file_content)
                        )
                        if exclude_attachments and filename in exclude_attachments:
                            continue
                        # Here we are using dict instead of list because in case of list
                        # we will have the following structure:
                        # Attachments{index}attachment_name
                        # which is not good for mapping, thus we are using dict

                        attachments_dict.update(
                            {
                                f"attachment_name_{index}": filename,
                                f"base64_encoded_content_{index}": (
                                    file_content.decode()
                                    if isinstance(file_content, bytes)
                                    else file_content
                                ),
                                f"md5_filehash_{index}": md5_file_hash,
                            }
                        )
                        index += 1

                    else:
                        # Extract filename from attachment
                        filename = self.extract_filename(attachment)
                        if exclude_attachments and filename in exclude_attachments:
                            continue
                        # Some emails can return an empty attachment.
                        # Validate that the attachment has a filename
                        if filename:
                            # Get attachment content - decode to raw
                            file_content = attachment.get_payload(decode=True)
                            md5_file_hash = hashlib.md5(file_content).hexdigest()

                            # In case of EML file - probably bug.
                            # TODO: This might be problematic. As .eml attachment (content-type of messade/rfc822)
                            # TODO: are considered multipart, then get_payload() will return None.
                            # TODO: The extraction of file_data is correct, and in most cases
                            # TODO: it will be encoded with base64, but it's not guaranteed,
                            # TODO: so we might have to extract the Content-Transfer-Encoding
                            # TODO: and parse accordingly.
                            if not file_content and ".eml" in filename:
                                file_data = attachment.get_payload()[0]
                                payload = file_data.get_payload()
                                md5_file_hash = hashlib.md5(payload).hexdigest()
                                file_content = b64decode(payload)

                            if encode_as_base64:
                                file_content = b64encode(file_content)

                            # Here we are using dict instead of list because in case of list
                            # we will have the following structure:
                            # Attachments{index}attachment_name
                            # which is not good for mapping, thus we are using dict

                            attachments_dict.update(
                                {
                                    f"attachment_name_{index}": filename,
                                    f"base64_encoded_content_{index}": (
                                        file_content.decode()
                                        if isinstance(file_content, bytes)
                                        else file_content
                                    ),
                                    f"md5_filehash_{index}": md5_file_hash,
                                }
                            )
                            index += 1

        return attachments_dict

    def convert_siemplify_ics_to_connector_msg(self, ics_content):
        parsed_ics_attachments = []
        cal = Calendar.from_ical(ics_content)

        for component in cal.walk("vevent"):
            subject = get_unicode_str(component.get("summary", ""))
            body = get_unicode_str(component.get("description", ""))
            location = get_unicode_str(component.get("location", ""))
            start = (
                component.get("dtstart", "").dt.isoformat()
                if component.get("dtstart", "")
                else None
            )
            end = (
                component.get("dtend", "").dt.isoformat()
                if component.get("dtend", "")
                else None
            )
            message_id = MESSAGE_ID_FORMAT.format(component.get("uid", ""))
            organizer = component.get("organizer", "").replace(EMAIL_PREFIX, "")
            attendees_list = component.get("attendee", "")
            attendees = DEFAULT_DIVIDER.join(
                [a.replace(EMAIL_PREFIX, "").strip() for a in attendees_list]
            )
            attachments_urls_list = self.extract_urls_from_ics_attachments(component)

            parsed_ics_attachment = {
                "subject": subject,
                "body": body,
                "location": location,
                "start_timestamp": start,
                "end_timestamp": end,
                "message_id": message_id,
                "from": organizer,
                "organizer": organizer,
                "to": attendees,
                "attendees": attendees,
            }

            if attachments_urls_list:
                parsed_ics_attachment["urls"] = attachments_urls_list

            parsed_ics_attachments.append(parsed_ics_attachment)

        return parsed_ics_attachments

    def extract_urls_from_ics_attachments(self, content):
        regex_object = re.compile(self.urls_regex)
        attachments = content.get("attach", [])
        attachments = attachments if isinstance(attachments, list) else [attachments]
        attachments_list = [
            check_url_enclosing(url.strip(CHARS_TO_STRIP))
            for url in regex_object.findall(
                DEFAULT_URLS_LIST_DELIMITER.join(attachments)
            )
            if "@" not in url
        ]
        return DEFAULT_URLS_LIST_DELIMITER.join(attachments_list)

    def extract_headers_value_from_message(
            self, msg: email.message.Message, headers: list[str]
    ) -> SingleJson:
        """
        Extract headers value from message.
        :param msg: {Message} An eml object
        :param headers: {list} List containing headers regexp.
        :return: {dict (connector_eml)} Extracted header according to headers regex
        """
        filtered_headers = {}
        if not headers:
            return filtered_headers

        for header in headers:
            _set_header_values(header, msg, filtered_headers)

        return filtered_headers

    def convert_siemplify_eml_to_connector_eml(
        self,
        eml_content: email.message.Message,
        convert_body_to_utf8: bool = False,
        convert_subject_to_utf8: bool = False,
        encode_attachments_as_base64: bool = True,
        convert_filenames_to_utf8: bool = True,
        is_v2_connector: bool = False,
        exclude_attachments: [str] = None,
        headers_to_add: [str] = None,
        private_key_path: str = None,
        certificate_path: str = None,
        ca_certificate_path: str = None,
        temp_folder_path: str = None,
    ) -> dict:
        """
        Convert a Siemplify EML object to connector EML object.
        Used for avoiding regressions.

        Args:
            eml_content (email.message.Message): An eml object
            convert_body_to_utf8 (bool): Return message body as utf-8 encoded str (
            Avoid regression).
            convert_subject_to_utf8 (bool): Return message subject as utf-8 encoded str(
            Avoid regression).
            encode_attachments_as_base64 (bool):  Whether to encode the attachments
            content with base64.
            convert_filenames_to_utf8 (bool): Return message filenames as utf-8
            encoded str.
            is_v2_connector (bool): Whether the data for ExchangeMailConnector2 or not.
            exclude_attachments (list): The list of the attachments names should
            be ignored
            headers_to_add (list): The list of the headers/header_regexp to add to the
            final result
            private_key_path (str): Path to private key file
            certificate_path (str): Path to key certificate file
            ca_certificate_path (str): Path to CA certificate file
            temp_folder_path (str): Path to temporary folder

        Returns:
            dict (connector_eml) The data of the eml
        """
        msg = email.message_from_bytes(eml_content)

        if is_v2_connector:
            msg = self.handle_smime_msg(
                msg,
                private_key_path,
                certificate_path,
                ca_certificate_path,
                temp_folder_path,
                original_msg_bytes=eml_content,
            )

        metadata = self.convert_eml_to_siemplify_eml(
            msg,
            convert_body_to_utf8=convert_body_to_utf8,
            convert_subject_to_utf8=convert_subject_to_utf8,
        )

        to = metadata.get(SIEMPLIFY_MAIL_DICT_TO_KEY)
        cc = metadata.get(SIEMPLIFY_MAIL_DICT_CC_KEY)
        bcc = metadata.get(SIEMPLIFY_MAIL_DICT_BCC_KEY)

        recipients = [recipient for recipient in itertools.chain(to, cc, bcc)]
        metadata["Recipients"] = ", ".join(recipients)
        if is_v2_connector:
            # Fix extraction of email addresses from headers
            to_raw = self.extract_email_addresses_from_msg(msg, "To")
            senders = self.extract_email_addresses_from_msg(msg, "From")
            sender_raw = senders[0] if senders else self.UNKNOWN_SENDER
            cc_raw = self.extract_email_addresses_from_msg(msg, "Cc")
            bcc_raw = self.extract_email_addresses_from_msg(msg, "Bcc")
            recipients_raw = [
                recipient for recipient in itertools.chain(to_raw, cc_raw, cc_raw)
            ]

            main_content = {
                "answer": metadata.get(SIEMPLIFY_MAIL_DICT_ANSWER_ID_KEY),
                "attachments": self._extract_attachments_from_eml(
                    msg,
                    encode_as_base64=encode_attachments_as_base64,
                    convert_utf8=convert_filenames_to_utf8,
                    exclude_attachments=exclude_attachments,
                ),
                "bcc": ",".join(metadata.get(SIEMPLIFY_MAIL_DICT_BCC_KEY, [])),
                "bcc_raw": ",".join(bcc_raw),
                "cc": ",".join(metadata.get(SIEMPLIFY_MAIL_DICT_CC_KEY, [])),
                "cc_raw": ",".join(cc_raw),
                "body": metadata.get(SIEMPLIFY_MAIL_DICT_RESOLVED_BODY_KEY),
                "date": metadata.get(SIEMPLIFY_MAIL_DICT_DATE_KEY),
                "email_uid": metadata.get(SIEMPLIFY_MAIL_DICT_EMAIL_ID_KEY),
                "html_body": metadata.get(SIEMPLIFY_MAIL_DICT_HTML_BODY_KEY),
                "in_reply_to": metadata.get(SIEMPLIFY_MAIL_DICT_IN_REPLY_TO_KEY),
                "message_id": metadata.get(SIEMPLIFY_MAIL_DICT_MESSAGE_ID_KEY),
                "plaintext_body": metadata.get(SIEMPLIFY_MAIL_DICT_PLAINTEXT_BODY_KEY),
                "receivers": ", ".join(recipients),
                "receivers_raw": ", ".join(recipients_raw),
                "reply_to": metadata.get(SIEMPLIFY_MAIL_DICT_IN_REPLY_TO_KEY),
                "sender": metadata.get(SIEMPLIFY_MAIL_DICT_SENDER_KEY),
                "sender_raw": sender_raw,
                "subject": metadata.get(SIEMPLIFY_MAIL_DICT_SUBJECT_KEY),
                "timestamp": metadata.get(SIEMPLIFY_MAIL_DICT_UNIXTIME_DATE_KEY),
                "to": ",".join(metadata.get(SIEMPLIFY_MAIL_DICT_TO_KEY, [])),
                "to_raw": ",".join(to_raw),
                SIEMPLIFY_MAIL_DICT_UNIXTIME_DATE_KEY: metadata.get(
                    SIEMPLIFY_MAIL_DICT_UNIXTIME_DATE_KEY
                ),
            }
            main_content.update(
                self.extract_headers_value_from_message(msg, headers_to_add)
            )
            return main_content
        return {
            "subject": metadata.get(SIEMPLIFY_MAIL_DICT_SUBJECT_KEY),
            "from": metadata.get(SIEMPLIFY_MAIL_DICT_SENDER_KEY),
            "to": ",".join(metadata.get(SIEMPLIFY_MAIL_DICT_TO_KEY, [])),
            "CC": ",".join(metadata.get(SIEMPLIFY_MAIL_DICT_CC_KEY, [])),
            "BCC": ",".join(metadata.get(SIEMPLIFY_MAIL_DICT_BCC_KEY, [])),
            "Recipients": ", ".join(recipients),
            "Date": metadata.get(SIEMPLIFY_MAIL_DICT_DATE_KEY),
            "body": metadata.get(SIEMPLIFY_MAIL_DICT_RESOLVED_BODY_KEY),
            "plaintext_body": metadata.get(SIEMPLIFY_MAIL_DICT_PLAINTEXT_BODY_KEY),
            "HTML Body": metadata.get(SIEMPLIFY_MAIL_DICT_HTML_BODY_KEY),
            "Attachments": self._extract_attachments_from_eml(
                msg,
                encode_as_base64=encode_attachments_as_base64,
                convert_utf8=convert_filenames_to_utf8,
            ),
            SIEMPLIFY_MAIL_DICT_UNIXTIME_DATE_KEY: metadata.get(
                SIEMPLIFY_MAIL_DICT_UNIXTIME_DATE_KEY
            ),
            "display_name": metadata.get(SIEMPLIFY_MAIL_DICT_NAMES_KEY, {}).get(
                metadata.get(SIEMPLIFY_MAIL_DICT_SENDER_KEY)
            ),
        }

    @staticmethod
    def extract_email_addresses_from_msg(message, header_name):
        """
        Extract addresses from email headers.
        This function replaces the emaildata.Metadata._address function due to incorrect extraction of the addresses for emails sent from Exchange
        Server. Instead, after the headers will be decoded (using the same functionality) we will pass it to email.utils.getaddresses() function
        for proper extraction of the email addresses.
        :param message: {email.message.Message} Email message
        :param header_name: {str} The header content to extract the addresses from
        :return: {[str]} List of extracted email addresses, excluding duplicates
        """

        def decode(text, encoding):
            """Decode a text. If an exception occurs when decoding returns the
            original text"""
            try:
                if isinstance(text, bytes):
                    return text.decode(encoding or "utf-8")
                return text
            except:
                return text_to_utf8(text)

        header_value = message[header_name]

        if not header_value:
            return []

        if isinstance(header_value, str):
            header_value = header_value.replace("\n", " ")

        pieces = email.header.decode_header(header_value)
        pieces = [decode(text, encoding) for text, encoding in pieces]
        addresses = sorted(
            list(
                set(
                    e
                    for realname, e in email.utils.getaddresses(
                        ["".join(pieces).strip()]
                    )
                    if e
                )
            )
        )
        return [address for address in addresses if "@" in address]

    def convert_eml_to_siemplify_eml(
        self,
        msg,
        include_raw_eml=False,
        convert_body_to_utf8=False,
        convert_subject_to_utf8=False,
        email_uid=None,
    ):
        """
        Create a Siemplify eml object from a given eml MIME (email.message.Message).
        The method is parsing the email.Message object relevant data and created a dict in Siemplify format.
        :param msg: {email.message.Message} The msg object
        :param include_raw_eml: {boolean} get the mail eml (in eml format)
        :param convert_body_to_utf8: {boolean} Return message body as utf-8 encoded str(Avoid regression).
        :param convert_subject_to_utf8: {boolean} Return message subject as utf-8 encoded str(Avoid regression).
        :param email_uid: {int} The uid of the email (in case the email was fetched from an IMAP server, like gmail)
        :return: {dict} The mail data
        """

        message_for_extractor = copy.deepcopy(msg)
        del message_for_extractor["Subject"]

        extractor = MetaData(message_for_extractor)
        # Start building "siemplify mail dict". base it on "email library dict"
        # It's assumed that message_id key is already there
        mail_dict = extractor.to_dict()

        mail_dict[SIEMPLIFY_MAIL_DICT_UNIXTIME_DATE_KEY] = (
            self.extract_unixtime_date_from_msg(msg.get("date"))
        )
        mail_dict[SIEMPLIFY_MAIL_DICT_DATE_KEY] = msg.get("date")

        subject = self.extract_subject(msg, convert_subject_to_utf8)

        if subject:
            subject = subject.strip()

        mail_dict[SIEMPLIFY_MAIL_DICT_SUBJECT_KEY] = (
            subject if subject else self.EMPTY_SUBJECT
        )

        mail_dict[SIEMPLIFY_MAIL_DICT_PLAINTEXT_BODY_KEY] = (
            self.extract_bodies_from_eml(msg, convert_body_to_utf8)[0]
        )
        mail_dict[SIEMPLIFY_MAIL_DICT_HTML_BODY_KEY] = self.extract_bodies_from_eml(
            msg, convert_body_to_utf8
        )[1]
        mail_dict[SIEMPLIFY_MAIL_DICT_EMAIL_ID_KEY] = email_uid

        if not mail_dict.get(SIEMPLIFY_MAIL_DICT_SENDER_KEY):
            mail_dict[SIEMPLIFY_MAIL_DICT_SENDER_KEY] = self.UNKNOWN_SENDER
        if not mail_dict.get(SIEMPLIFY_MAIL_DICT_TO_KEY):
            mail_dict[SIEMPLIFY_MAIL_DICT_TO_KEY] = []
        if not mail_dict.get(SIEMPLIFY_MAIL_DICT_CC_KEY):
            mail_dict[SIEMPLIFY_MAIL_DICT_CC_KEY] = []
        if not mail_dict.get(SIEMPLIFY_MAIL_DICT_BCC_KEY):
            mail_dict[SIEMPLIFY_MAIL_DICT_BCC_KEY] = []

        if mail_dict[SIEMPLIFY_MAIL_DICT_PLAINTEXT_BODY_KEY]:
            mail_dict[SIEMPLIFY_MAIL_DICT_RESOLVED_BODY_KEY] = mail_dict[
                SIEMPLIFY_MAIL_DICT_PLAINTEXT_BODY_KEY
            ]
        else:
            # Can't know the original charset of the body - try and hope for the best.
            mail_dict[SIEMPLIFY_MAIL_DICT_RESOLVED_BODY_KEY] = self.render_html_body(
                mail_dict[SIEMPLIFY_MAIL_DICT_HTML_BODY_KEY]
            )

        # Try extracting the answer
        try:
            match = re.search(
                ANSWER_PLACEHOLDER_PATTERN,
                mail_dict[SIEMPLIFY_MAIL_DICT_RESOLVED_BODY_KEY],
            )
            if match:
                mail_dict[SIEMPLIFY_MAIL_DICT_ANSWER_ID_KEY] = match.group()
            else:
                mail_dict[SIEMPLIFY_MAIL_DICT_ANSWER_ID_KEY] = ""
        except Exception:
            mail_dict[SIEMPLIFY_MAIL_DICT_ANSWER_ID_KEY] = ""

        if include_raw_eml:
            # original message as string
            mail_dict["original_message"] = message_as_string(msg, logger=self.logger)

        return mail_dict

    def extract_bodies_from_eml(self, msg, convert_body_to_utf8=False):
        """
        Extracts bodies (plaintext + html) from an email.message.Message (eml mimes).
        :param msg: {email.message.Message} An eml object
        :param convert_body_to_utf8: {bool} True to return body as ut8 encoded string(Avoid regression).
        :return: {tuple} Text body, Html body, count of parts of the emails
        """
        html_body = ""
        text_body = ""
        count = 0

        if not msg.is_multipart():
            if self.is_attachment(msg):
                return text_body, html_body, count

            # Not an attachment!
            # See where this belongs - text_body or html_body
            content_type = msg.get_content_type()
            message_payload = msg.get_payload(decode=True)
            charset = get_charset(msg)

            if message_payload is not None:
                if content_type == "text/plain":
                    text_body += self.decode_by_charset(message_payload, charset)

                elif content_type == "text/html":
                    html_body += self.decode_by_charset(message_payload, charset)

            return text_body, html_body, 1

        # This IS a multipart message.
        # So, we iterate over it and call extract_bodies_from_eml() recursively for
        # each part.
        payload = msg.get_payload()
        messages = payload if payload is not None else []
        for part_msg in messages:
            # Verify that the mime part is not an attachment to avoid body containing attachment data
            if not self.is_attachment(part_msg):
                # Th part is a new Message object which goes back to extract_bodies_from_eml
                part_text_body, part_html_body, part_count = (
                    self.extract_bodies_from_eml(part_msg)
                )
                text_body += part_text_body
                html_body += part_html_body
                count += part_count

        return text_body, html_body, count

    def extract_subject(self, msg, convert_utf8=False):
        """
        Extract message subject from email message.
        :param msg: {Message} Message object.
        :param convert_utf8: {bool} True to convert subject to utf-8 encoded string.
        :return: {string} Subject text.
        """
        raw_subject = msg.get(MAIL_SUBJECT_KEY)

        return decode_header_value(raw_subject)

    @staticmethod
    def extract_unixtime_date_from_msg(date_str, default_value=1):
        """
        Extract the date of the msg in unixtime
        :param date_str: {str} The date string to parse
        :param default_value: {long} The default value to return on failure. If not passed (None, 0, any False value) - an exception will be raised on failure.
        :return: {long} The unixtime of the message. If failed parsing - return 1.
        """
        try:
            if date_str:
                date_tuple = email.utils.parsedate_tz(date_str)
                if date_tuple:
                    # Returns time in seconds, not in milliseconds
                    return email.utils.mktime_tz(date_tuple) * 1000

            return default_value

        except Exception:
            return default_value

    # TODO: Deprecated - not used anymore
    @staticmethod
    def fetch_message_charset(message):
        """
        Fetch the charset of the payload of the message.
        :param message: {Message} Message object.
        :return: {string} Payload charset.
        """
        charset = message.get_content_charset()

        if charset in ENCODING_MAPPING:
            return ENCODING_MAPPING.get(charset)
        return charset

    @staticmethod
    def _build_html_2_text_obj():
        """
        Create a HTML2Text object
        :return: {html2text.HTML2Text} The HTMl2Text object
        """
        html_renderer = html2text.HTML2Text()
        # Configuration was decided by Product Team
        html_renderer.ignore_tables = True
        html_renderer.protect_links = True
        html_renderer.ignore_images = False
        html_renderer.ignore_links = False
        return html_renderer

    @staticmethod
    def render_html_body(html_body):
        """
        Render html body to plain text plain
        :param html_body: {str} The HTML body of the email
        :return: {str} Plain text rendered HTML
        """
        try:
            html_renderer = EmailUtils._build_html_2_text_obj()
            return html_renderer.handle(html_body)

        except Exception:
            # HTML2Text is not performing well on non-ASCII str. On failure - try to decode the str to unicode
            # using utf8 encoding. If failed - return a proper message.
            try:
                # HTML2Text object shouldn't be used twice - it can cause problems and errors according to google
                # Therefore rebuild the object
                html_renderer = EmailUtils._build_html_2_text_obj()
                html_body = html_body.decode("utf8")
                # Encode back to utf8
                return html_renderer.handle(html_body).encode("utf8")
            except Exception as e:
                return f"Failed rendering HTML. Error: {str(e)}"

    def convert_siemplify_msg_to_connector_msg(
        self,
        msg_content,
        convert_body_to_utf8=False,
        convert_subject_to_utf8=False,
        encode_attachments_as_base64=True,
        convert_filenames_to_utf8=True,
        is_v2_connector=False,
    ):
        """
        Convert Siemplify MSG object to connector MSG object. Used to avoid regressions.
        :param msg_content: {extract_msg.message.Message} An msg object
        :param convert_body_to_utf8: {boolean} Return message body as utf-8 encoded str(Avoid regression).
        :param convert_subject_to_utf8: {boolean} Return message subject as utf-8 encoded str(Avoid regression).
        :param convert_filenames_to_utf8: {boolean} Return message filenames as utf-8 encoded str.
        :param encode_attachments_as_base64: {boolean} Whether to encode the attachments content with base64.
        :param is_v2_connector: {boolean} Whether the data for ExchangeMailConnector2 or not.
        :return: {dict (connector_msg)} The data of the .msg
        """

        msg = extract_msg.Message(msg_content)
        # Build the Siemplify MSG object
        metadata = self.convert_outlook_msg_to_siemplify_msg(
            msg,
            convert_body_to_utf8=convert_body_to_utf8,
            convert_subject_to_utf8=convert_subject_to_utf8,
        )

        to = metadata.get(SIEMPLIFY_MAIL_DICT_TO_KEY)
        cc = metadata.get(SIEMPLIFY_MAIL_DICT_CC_KEY)
        bcc = metadata.get(SIEMPLIFY_MAIL_DICT_BCC_KEY)

        recipients = [recipient for recipient in itertools.chain(to, cc, bcc)]
        metadata["Recipients"] = ", ".join(recipients)
        if is_v2_connector:
            return {
                "answer": metadata.get(SIEMPLIFY_MAIL_DICT_ANSWER_ID_KEY),
                "attachments": self._extract_attachment_from_outlook_msg(
                    msg,
                    encode_as_base64=encode_attachments_as_base64,
                    convert_utf8=convert_filenames_to_utf8,
                ),
                "bcc": ",".join(metadata.get(SIEMPLIFY_MAIL_DICT_BCC_KEY, [])),
                "cc": ",".join(metadata.get(SIEMPLIFY_MAIL_DICT_CC_KEY, [])),
                "body": metadata.get(SIEMPLIFY_MAIL_DICT_RESOLVED_BODY_KEY),
                "date": metadata.get(SIEMPLIFY_MAIL_DICT_DATE_KEY),
                "email_uid": metadata.get(SIEMPLIFY_MAIL_DICT_EMAIL_ID_KEY),
                "html_body": metadata.get(SIEMPLIFY_MAIL_DICT_HTML_BODY_KEY),
                "in_reply_to": metadata.get(SIEMPLIFY_MAIL_DICT_IN_REPLY_TO_KEY),
                "message_id": metadata.get(SIEMPLIFY_MAIL_DICT_MESSAGE_ID_KEY),
                "plaintext_body": metadata.get(SIEMPLIFY_MAIL_DICT_PLAINTEXT_BODY_KEY),
                "receivers": ", ".join(recipients),
                "reply_to": metadata.get(SIEMPLIFY_MAIL_DICT_IN_REPLY_TO_KEY),
                "sender": metadata.get(SIEMPLIFY_MAIL_DICT_SENDER_KEY),
                "subject": metadata.get(SIEMPLIFY_MAIL_DICT_SUBJECT_KEY),
                "timestamp": metadata.get(SIEMPLIFY_MAIL_DICT_UNIXTIME_DATE_KEY),
                "to": ",".join(metadata.get(SIEMPLIFY_MAIL_DICT_TO_KEY, [])),
                SIEMPLIFY_MAIL_DICT_UNIXTIME_DATE_KEY: metadata.get(
                    SIEMPLIFY_MAIL_DICT_UNIXTIME_DATE_KEY
                ),
            }
        return {
            "subject": metadata.get(SIEMPLIFY_MAIL_DICT_SUBJECT_KEY),
            "from": metadata.get(SIEMPLIFY_MAIL_DICT_SENDER_KEY),
            "to": ",".join(metadata.get(SIEMPLIFY_MAIL_DICT_TO_KEY, [])),
            "CC": ",".join(metadata.get(SIEMPLIFY_MAIL_DICT_CC_KEY, [])),
            "BCC": ",".join(metadata.get(SIEMPLIFY_MAIL_DICT_BCC_KEY, [])),
            "Recipients": ", ".join(recipients),
            "Date": metadata.get(SIEMPLIFY_MAIL_DICT_DATE_KEY).isoformat(),
            "body": metadata.get(SIEMPLIFY_MAIL_DICT_RESOLVED_BODY_KEY),
            "plaintext_body": metadata.get(SIEMPLIFY_MAIL_DICT_PLAINTEXT_BODY_KEY),
            "HTML Body": metadata.get(SIEMPLIFY_MAIL_DICT_HTML_BODY_KEY),
            "Attachments": self._extract_attachment_from_outlook_msg(
                msg,
                encode_as_base64=encode_attachments_as_base64,
                convert_utf8=convert_filenames_to_utf8,
            ),
            SIEMPLIFY_MAIL_DICT_UNIXTIME_DATE_KEY: metadata.get(
                SIEMPLIFY_MAIL_DICT_UNIXTIME_DATE_KEY
            ),
            "display_name": ",".join(
                metadata.get(SIEMPLIFY_MAIL_DICT_DISPLAY_NAME_KEY, [])
            ),
        }

    def convert_outlook_msg_to_siemplify_msg(
        self,
        msg,
        convert_body_to_utf8=False,
        convert_subject_to_utf8=False,
        email_uid=None,
    ):
        """
        Create a Siemplify msg object from a given outlook msg (extract_msg.message.Message).
        The method is parsing the extract_msg.Message object relevant data and created a dict in Siemplify format.
        :param msg: {extract_msg.message.Message} The msg object
        :param convert_body_to_utf8: {boolean} Return message body as utf-8 encoded str(Avoid regression).
        :param convert_subject_to_utf8: {boolean} Return message subject as utf-8 encoded str(Avoid regression).
        :param email_uid: {int} The uid of the email (in case the email was fetched from an IMAP server, like gmail)
        :return: {dict (siemplify_msg)} The mail data
        """
        mail_dict = dict()
        mail_dict[SIEMPLIFY_MAIL_DICT_UNIXTIME_DATE_KEY] = (
            self.extract_unixtime_date_from_msg(msg.date)
        )
        mail_dict[SIEMPLIFY_MAIL_DICT_DATE_KEY] = datetime(*msg.parsedDate[0:6])
        mail_dict[SIEMPLIFY_MAIL_DICT_TIMESTAMP_KEY] = int(time.mktime(msg.parsedDate))
        mail_dict[SIEMPLIFY_MAIL_DICT_SENDER_KEY] = self.extract_addresses(
            msg.sender or ""
        )
        mail_dict[SIEMPLIFY_MAIL_DICT_TO_KEY] = self.extract_addresses(msg.to)
        mail_dict[SIEMPLIFY_MAIL_DICT_CC_KEY] = self.extract_addresses(msg.cc)
        mail_dict[SIEMPLIFY_MAIL_DICT_BCC_KEY] = self.extract_addresses(
            msg.header.get("bcc")
        )
        mail_dict[SIEMPLIFY_MAIL_DICT_REPLY_TO_KEY] = msg.inReplyTo
        mail_dict[SIEMPLIFY_MAIL_DICT_IN_REPLY_TO_KEY] = msg.inReplyTo
        mail_dict[SIEMPLIFY_MAIL_DICT_MESSAGE_ID_KEY] = msg.messageId
        mail_dict[SIEMPLIFY_MAIL_DICT_EMAIL_ID_KEY] = email_uid
        mail_dict[SIEMPLIFY_MAIL_DICT_DISPLAY_NAME_KEY] = self.extract_names(
            msg.sender or ""
        )

        # Construct the receivers from to + cc + bcc addresses
        mail_dict[SIEMPLIFY_MAIL_DICT_RECEIVERS_KEY] = set()
        mail_dict[SIEMPLIFY_MAIL_DICT_RECEIVERS_KEY].union(
            mail_dict[SIEMPLIFY_MAIL_DICT_TO_KEY]
        )
        mail_dict[SIEMPLIFY_MAIL_DICT_RECEIVERS_KEY].union(
            mail_dict[SIEMPLIFY_MAIL_DICT_CC_KEY]
        )
        mail_dict[SIEMPLIFY_MAIL_DICT_RECEIVERS_KEY].union(
            mail_dict[SIEMPLIFY_MAIL_DICT_BCC_KEY]
        )
        mail_dict[SIEMPLIFY_MAIL_DICT_SUBJECT_KEY] = get_unicode_str(msg.subject)
        mail_dict[SIEMPLIFY_MAIL_DICT_PLAINTEXT_BODY_KEY] = get_unicode_str(msg.body)

        try:
            mail_dict[SIEMPLIFY_MAIL_DICT_HTML_BODY_KEY] = (
                self.extract_html_body_from_outlook_msg(msg, convert_body_to_utf8)
            )
        except Exception as e:
            mail_dict[SIEMPLIFY_MAIL_DICT_HTML_BODY_KEY] = (
                f"Unable to extract HTML body. Error: {e}"
            )
        if mail_dict[SIEMPLIFY_MAIL_DICT_PLAINTEXT_BODY_KEY]:
            mail_dict[SIEMPLIFY_MAIL_DICT_RESOLVED_BODY_KEY] = mail_dict[
                SIEMPLIFY_MAIL_DICT_PLAINTEXT_BODY_KEY
            ]
        else:
            # Can't know the original charset of the body - try and hope for the best.
            mail_dict[SIEMPLIFY_MAIL_DICT_RESOLVED_BODY_KEY] = self.render_html_body(
                mail_dict[SIEMPLIFY_MAIL_DICT_HTML_BODY_KEY]
            )

        # Try extracting the answer
        try:
            match = re.search(
                ANSWER_PLACEHOLDER_PATTERN,
                mail_dict[SIEMPLIFY_MAIL_DICT_RESOLVED_BODY_KEY],
            )
            if match:
                mail_dict[SIEMPLIFY_MAIL_DICT_ANSWER_ID_KEY] = match.group()
            else:
                mail_dict[SIEMPLIFY_MAIL_DICT_ANSWER_ID_KEY] = ""
        except Exception:
            mail_dict[SIEMPLIFY_MAIL_DICT_ANSWER_ID_KEY] = ""

        return mail_dict

    @staticmethod
    def extract_html_body_from_outlook_msg(msg, convert_body_to_utf8=False):
        """
        Extract the body from extract_msg.message.Message (according to product defined logic). Extract HTML if available,
        or extract the HTML from the RTF, based on product defined logic.
        :param msg: {extract_msg.message.Message} The message obj
        :param convert_body_to_utf8: {bool} Return message body as utf-8 encoded str(Avoid regression).
        :return: {str/unicode} The extracted body (unicode of convert_body_to_utf8 is False)
        """
        if msg.htmlBody:
            return get_unicode_str(msg.htmlBody)
        else:
            # decompress the rtf content of the msg
            rtf_content = compressed_rtf.decompress(msg.compressedRtf)
            rtf_file = BytesIO()
            rtf_file.write(rtf_content)

            rdf_handler = Rtf15Reader.read(rtf_file)
            html_body = XHTMLWriter.write(rdf_handler, pretty=True).read()
            return get_unicode_str(html_body)

    @staticmethod
    def extract_addresses_with_names(header_content):
        """
        Extract addresses and corresponding display names from email headers. Based on the _address method of email.Metadata.
        :param header_content: {str} The header content to extract the addresses from
        :return: {list} The extracted addresses (list of unicodes)
        """

        def decode(text, encoding):
            """Decode a text. If an exception occurs when decoding returns the
            original text"""
            if encoding is None:
                return get_unicode_str(text)
            try:
                return text.decode(encoding)
            except Exception:
                return get_unicode_str(text)

        result = dict()
        pieces = email.header.decode_header(header_content or "")
        pieces = [decode(text, encoding) for text, encoding in pieces]
        header_value = "".join(pieces).strip()
        name, address = email.utils.parseaddr(header_value)
        while address:
            result[address] = name or None
            index = header_value.find(address) + len(address)
            if index >= len(header_value):
                break
            if header_value[index] == ">":
                index += 1
            if index >= len(header_value):
                break
            if header_value[index] == ",":
                index += 1
            header_value = header_value[index:].strip()
            name, address = email.utils.parseaddr(header_value)

        return result

    def extract_addresses(self, header_content):
        """
        Extract addresses from email headers. Based on the _address method of email.Metadata.
        :param header_content: {str} The header content to extract the addresses from
        :return: {list} The extracted addresses (list of unicodes)
        """
        result = self.extract_addresses_with_names(header_content)
        return [
            address for address in result.keys() if address and address != str(None)
        ]

    def extract_names(self, header_content):
        """
        Extract display names corresponding to addresses from email headers. Based on the _address method of email.Metadata.
        :param header_content: {str} The header content to extract the addresses from
        :return: {list} The extracted names
        """
        result = self.extract_addresses_with_names(header_content)
        return [name for name in result.values() if name and name != str(None)]

    def _extract_attachment_from_outlook_msg(
        self, msg, encode_as_base64=False, convert_utf8=True
    ):
        """
        Extract the attachments (filename: file_content} from an extract_msg.messageMessage object (parsed outlook msg)
        :param msg: {extract_msg.messageMessage} the msg to extract from
        :param encode_as_base64: {bool} Whether to encode the attachments content with base64 or not
        :param convert_utf8: {bool} Whether to convert the filename to utf8
        :return: {dict} The extracted attachments (filename: content)
        """
        attachments_dict = {}

        for attachment in msg.attachments:
            if attachment.type == DATA_ATTACHMENT:
                # Extract filename
                if convert_utf8:
                    filename = attachment.longFilename.encode("utf8")
                else:
                    filename = attachment.longFilename

                # The content returned raw - no way of knowing the encoding of the attachment.
                # So leave it like that
                file_content = attachment.data

                if encode_as_base64:
                    file_content = b64encode(file_content)

                attachments_dict.update({filename: file_content})
            else:
                attachments_dict.update(
                    {get_unicode_str(attachment.data.subject): INNER_MSG_NOT_SUPPORTED}
                )

        return attachments_dict

    @staticmethod
    def decode_by_charset(bytes_string, charset, default_charset="latin1"):
        """
        Decode bytes string by a given charset
        :param bytes_string: {bytes} bytes string
        :param charset: {str} charset to use for decoding
        :param default_charset: {str} default charset to use when given charset is not supported
        :return: {str} decoded string
        """
        try:
            return bytes_string.decode(charset)
        except:
            try:
                # If there is an exception with provided charset, try to decode with default charset
                return bytes_string.decode(default_charset)
            except:
                try:
                    # If there is an exception also with default charset,
                    # decode with provided charset ignoring the errors
                    return bytes_string.decode(charset, "ignore")
                except:
                    # If there is an exception with the provided charset by ignoring errors,
                    # decode with default charset ignoring the errors
                    return bytes_string.decode(default_charset, "ignore")

    def handle_smime_msg(
        self,
        msg: email.message.Message,
        private_key_path: str,
        certificate_path: str,
        ca_certificate_path: str,
        temp_folder_path: str,
        original_msg_bytes: bytes | None = None,
    ) -> email.message.Message:
        """
        Check if message is encrypted/signed and decrypt/verify it

        Args:
            msg (email.message.Message): Message object
            private_key_path (str): Path to private key file
            certificate_path (str): Path to key certificate file
            ca_certificate_path (str): Path to CA certificate file
            temp_folder_path (str): Path to temporary folder

        Returns:
            email.message.Message: Message object with decrypted/verified content
        """
        smime_type = self.get_smime_type(msg)

        if not smime_type:
            return msg

        message_file_path = os.path.join(temp_folder_path, "saved-message.msg")

        if original_msg_bytes is not None:
            with open(message_file_path, "wb") as f:
                f.write(original_msg_bytes)
        else:
            save_content_to_file(message_file_path, msg.as_string())

        return self.process_smime_message(
            msg,
            smime_type,
            message_file_path,
            private_key_path,
            certificate_path,
            ca_certificate_path,
        )

    def process_smime_message(
        self,
        msg: email.message.Message,
        smime_type: SmimeType,
        message_file_path: str,
        private_key_path: str,
        certificate_path: str,
        ca_certificate_path: str,
    ) -> email.message.Message:
        """
        Process smime message to decrypt and/or verify

        Args:
            msg (email.message.Message): Message object
            smime_type (SmimeType): SmimeType enum item
            message_file_path (str): Path to SMIME message file
            private_key_path (str): Path to private key file
            certificate_path (str): Path to key certificate file
            ca_certificate_path (str): Path to CA certificate file

        Returns:
            email.message.Message: Decrypted and/or verified Message object
        """
        try:
            if smime_type == SmimeType.ENCRYPTED:
                msg = self.decrypt_message(
                    msg, message_file_path, private_key_path, certificate_path
                )

                smime_type = self.get_smime_type(msg)

            if smime_type == SmimeType.SIGNED:
                msg = verify_message(msg, message_file_path, ca_certificate_path)

            return msg

        except Exception as e:
            raise SMIMEMailError(e) from e

    def get_smime_type(self, msg: email.message.Message) -> SmimeType | None:
        """
        Check if the message is S/MIME encrypted, signed or not and return smime type

        Args:
            msg (email.message.Message): Message object

        Returns:
            SmimeType | None: SmimeType enum item if it is SMIME message or None
        """
        smime_type = None
        content_type = msg.get("Content-Type", None)
        self.logger.info(f"msg content-type::: {content_type}")

        if content_type is not None:
            mime_type = content_type.split(";")[0]
            # Check for common S/MIME content types
            if mime_type.lower() in ["application/pkcs7-mime"]:
                smime_type = SmimeType.ENCRYPTED

            elif (
                mime_type.lower() in ["multipart/signed"]
                or "signed-data" in content_type.lower()
            ):
                smime_type = SmimeType.SIGNED

        return smime_type

    @staticmethod
    def decrypt_message(
        msg: email.message.Message,
        message_file_path: str,
        private_key_path: str,
        certificate_path: str,
    ) -> email.message.Message:
        """
        Decrypt encrypted message

        Args:
            msg (email.message.Message): Message object with encrypted content
            message_file_path (str): Path to message file
            private_key_path (str): Path to private key file
            certificate_path (str): Path to key certificate file

        Returns:
            email.message.Message: Message object with decrypted content

        Raises:
            FileError: raise exception if private_key_path or certificate_path missing
            SMIMEMailError: raise exception in case of subprocess error
        """
        if not private_key_path or not certificate_path:
            raise FileError(
                "Private key and Certificate is required to decrypt SMIME "
                "encrypted message."
            )

        decrypt_command = [
            "openssl",
            "smime",
            "-decrypt",
            "-in",
            message_file_path,
            "-out",
            message_file_path,
            "-inkey",
            private_key_path,
            "-certfile",
            certificate_path,
        ]

        try:
            subprocess.run(decrypt_command, capture_output=True, text=True, check=True)

            with open(message_file_path, "r", encoding="utf-8") as file:
                extracted_msg = email.message_from_string(file.read())

                for key, value in msg.items():
                    extracted_msg.add_header(key, value)

                return extracted_msg

        except subprocess.CalledProcessError as e:
            raise SMIMEMailError(
                f"Failed to decrypt SMIME mail. Error: {e.stderr}"
            ) from e

    def get_extracted_attachments_from_msg(
        self, msg: email.message.Message
    ) -> [FileAttachment]:
        """
        Extract attachments from message and return them as a list of FileAttachments

        Args:
            msg (email.message.Message): Message to extract attachments from

        Returns:
            [FileAttachment]: list of FileAttachments objects
        """
        attachments = self._extract_attachments_from_eml(msg, encode_as_base64=True)

        return [
            FileAttachment(
                name=attachment.get("attachment_name"),
                content=base64.b64decode(
                    attachment.get("base64_encoded_content")
                )
            )
            for attachment in flat_dict_to_list(attachments)
        ]


def verify_message(
    msg: email.message.Message, message_file_path: str, ca_certificate_path: str
) -> email.message.Message:
    """
    Verify signed message

    Args:
        msg (email.message.Message): Message object with signed content
        message_file_path (str): Path to message file
        ca_certificate_path (str): Path to CA certificate file

    Returns:
        email.message.Message: Message object with verified content

    Raises:
        FileError: raise exception if ca_certificate_path missing
        SMIMEMailError: raise exception in case of subprocess error
    """
    if not ca_certificate_path:
        raise FileError("CA certificate is required to verify SMIME signed message.")

    verify_command = [
        "openssl",
        "smime",
        "-verify",
        "-in",
        message_file_path,
        "-CAfile",
        ca_certificate_path,
        "-out",
        message_file_path,
    ]

    try:
        subprocess.run(verify_command, capture_output=True, text=True, check=True)

        with open(message_file_path, "r", encoding="utf-8") as file:
            extracted_msg = email.message_from_string(file.read())

            for key, value in msg.items():
                extracted_msg.add_header(key, value)

            return extracted_msg

    except subprocess.CalledProcessError as e:
        raise SMIMEMailError(f"Failed to verify SMIME mail. Error: {e.stderr}") from e


def create_account_rule(
    account,
    rule_name,
    condition,
    action,
    items
):
    folder_id = account.junk.id if action == "mark_as_junk" else None

    return UpdateInboxRules(account=account).call(
        operation="create",
        rule_name=rule_name,
        condition=condition,
        action=action,
        items=items,
        folder_id=folder_id
    )

def update_account_rule(
    account,
    rule_id,
    rule_name,
    condition,
    action,
    items
):
    folder_id = account.junk.id if action == "mark_as_junk" else None

    return UpdateInboxRules(account=account).call(
        operation="update",
        rule_id=rule_id,
        rule_name=rule_name,
        condition=condition,
        action=action,
        items=items,
        folder_id=folder_id
    )

def delete_account_rule(
    account,
    rule_id
):
    return UpdateInboxRules(account=account).call(
        operation="delete",
        rule_id=rule_id
    )


def is_encoded_header(header_value: str) -> bool:
    decoded_parts = email.header.decode_header(header_value)
    return any(isinstance(part, bytes) for part, encoding in decoded_parts if encoding)


def decode_header_string(header_value: str) -> str:
    """Decodes a header string that may contain RFC 2047 encoded-words.

    This function handles header values that are encoded according to RFC 2047.
    It decodes each part of the header, handling various encodings and potential
    decoding errors. It then concatenates the decoded parts into a single string.

    Args:
        header_value (str): The header value to decode.

    Returns:
        str: The decoded header string.
    """
    header_value = header_value.replace("\r\n", "")
    decoded_header_parts = email.header.decode_header(header_value)
    decoded_parts = []
    for part, encoding in decoded_header_parts:
        if isinstance(part, bytes):
            try:
                part = part.decode(encoding or "raw-unicode-escape")

            except LookupError:
                encoding = encoding.rstrip("-i").rstrip("-I")
                part = part.decode(encoding)

        decoded_parts.append(part)

    return "".join(decoded_parts)


def _set_header_values(
    header: str,
    msg: email.message.Message,
    filtered_headers: SingleJson
) -> None:
    """
    Set header values in filtered_headers dictionary.

    Args:
        header (str): header name to be added to the event.
        msg (email.message.Message): message object.
        filtered_headers (SingleJson): dictionary to store header values.
    """
    r = re.compile(header)
    header_keys = msg.keys()
    matched_keys = list(filter(r.match, header_keys))
    for key in matched_keys:
        value = msg.get(key)
        filtered_headers[key] = _get_header_value(value)

def _get_header_value(value: str) -> str:
    if isinstance(value, str) and is_encoded_header(value):
        return decode_header_string(value)

    return str(value)
