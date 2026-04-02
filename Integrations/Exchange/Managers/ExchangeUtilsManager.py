from __future__ import annotations
import base64
import binascii
import os
from collections import defaultdict
import pytz

from Siemplify import Siemplify
from SiemplifyUtils import utc_now, convert_string_to_datetime, convert_timezone
from datetime import timedelta
from exceptions import ExchangeException, InvalidBase64ParameterException
import urllib.parse


def get_time_filters(start_time_string, end_time_string, minutes_backwards):
    """
    Get start and end datetime
    :param start_time_string: {str} Start time string
    :param end_time_string: {str} End time string
    :param minutes_backwards: {int} Time backwards in minutes
    :return: {tuple} start and end datetime
    """
    start_time, end_time = None, None

    if start_time_string:
        start_time = convert_string_to_utc_datetime(start_time_string)
        end_time = (
            convert_string_to_utc_datetime(end_time_string) if end_time_string else None
        )
    elif minutes_backwards:
        start_time = utc_now().replace(tzinfo=pytz.utc) - timedelta(
            minutes=int(minutes_backwards)
        )

    if start_time and end_time and start_time > end_time:
        raise Exception("End Time should be later than Start Time")

    return start_time, end_time


def convert_string_to_utc_datetime(datetime_string):
    """
    Convert datetime string to utc datetime object
    :param datetime_string: {str} Datetime string
    :return: {Datetime} Datetime object
    """
    return convert_timezone(convert_string_to_datetime(datetime_string), "UTC").replace(
        tzinfo=pytz.utc
    )


def is_invalid_prefix(prefix):
    """
    Validate prefix string
    :param prefix: {str} Prefix to validate
    :return: {bool} True if invalid, False otherwise
    """
    return " " in prefix


def transform_dict_keys(original_dict, prefix, suffix, keys_to_except=[]):
    """
    Transform dict keys by adding prefix and suffix
    :param original_dict: {dict} Dict to transform keys
    :param prefix: {str} Prefix for the keys
    :param suffix: {str} Suffix for the keys
    :param keys_to_except: {list} The list of keys which shouldn't be transformed
    :return: {dict} The transformed dict
    """
    if prefix and suffix:
        return {
            f"{prefix}_{key}_{suffix}" if key not in keys_to_except else key: value
            for key, value in original_dict.items()
        }
    elif prefix:
        return {
            f"{prefix}_{key}" if key not in keys_to_except else key: value
            for key, value in original_dict.items()
        }

    return original_dict


def save_file(file_content, file_path):
    """
    Decode file content and save as file
    :param file_content: {str} File base64 content
    :param file_path: {str} File path
    :return: {str} File path
    """
    try:
        file_content = base64.b64decode(file_content).decode()
        with open(file_path, "w") as f:
            f.write(file_content)
            f.close()
        return file_path
    except Exception as e:
        raise ExchangeException(f"File Error: {e}")


def delete_files(siemplify_logger, file_paths):
    """
    Delete files
    :param siemplify_logger: Siemplify logger
    :param file_paths: {list} List of file paths to delete
    :return: {void}
    """
    for file_path in file_paths:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception as e:
                siemplify_logger.error(f"Unable to delete file {file_path}.")
                siemplify_logger.exception(e)


def convert_comma_separated_to_list(comma_separated):
    """
    Convert comma-separated string to list
    :param comma_separated: String with comma-separated values
    :return: List of values
    """
    return (
        [item.strip() for item in comma_separated.split(",")] if comma_separated else []
    )


def decode_url(url):
    """
    Decode encoded url
    :param url: {str} encoded url
    :return: {str} decoded url
    """
    return urllib.parse.unquote_plus(url)


def save_file_in_temp_folder(
    chronicle_soar: Siemplify,
    file_content: str,
    file_name: str,
    parameter_name: str
) -> str:
    """
    Save content to file in temp folder

    Args:
        chronicle_soar (Siemplify): Chronicle SOAR SDK object
        file_content (str): file content to save
        file_name (str): file name to save
        parameter_name (str): parameter name containing file content

    Returns:
        str: saved file path
    """
    try:
        file_content = base64.b64decode(file_content).decode()
        file_path = os.path.join(chronicle_soar.get_temp_folder_path(), file_name)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(file_content)

        return str(file_path)

    except (ValueError, binascii.Error) as e:
        raise InvalidBase64ParameterException(
            f"Invalid value was provided for parameter {parameter_name}. "
            f"Error: {e}"
        ) from e


def save_content_to_file(file_path: str, content: str):
    """
    Save content to file

    Args:
        file_path (str): file path to save
        content (str): content to save to file
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def flat_dict_to_list(flat_dict: dict[str, str]) -> list[dict[str, str]]:
    """
    Convert flat dict to list

    Args:
        flat_dict (dict[str, str]): flat dict to convert

    Returns:
        list[dict[str, str]]: converted list
    """
    grouped_items = defaultdict(dict)

    for key, value in flat_dict.items():
        index = key.split("_")[-1]
        grouped_items[index][key[:-len(index) - 1]] = value

    return list(grouped_items.values())
