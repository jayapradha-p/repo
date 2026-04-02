from unicodedata import bidirectional

from TIPCommon.extraction import extract_action_param, extract_configuration_param

from constants import (
    DECRYPT_CA_CERTIFICATE_FILE_PATH,
    DECRYPT_KEY_CERTIFICATE_FILE_PATH,
    DECRYPT_PRIVATE_KEY_FILE_PATH,
)
from ExchangeManager import ExchangeManager, ExchangeManagerV2, SmimeAuth
from ExchangeUtilsManager import save_file_in_temp_folder


def extract_action_parameter(
    siemplify,
    param_name,
    default_value=None,
    input_type=str,
    is_mandatory=False,
    print_value=False,
):
    """
    Wraps common call to TIPCommon.extract_action_param for convenience
    :param siemplify: {SiemplifyAction} Instance of the SiemplifyAction
    :param param_name: {str} Name of the integration configuration parameter
    :param default_value: {object} Default value depending on the input_type
    :param input_type: {type} Type of the expected parameter
    :param is_mandatory: {bool} True - method would raise an exception, if parameter is missing, False - no exception.
    :param print_value: {bool} Print extracted parameter value to the log
    :return: {object} Value of target type
    """
    return extract_action_param(
        siemplify=siemplify,
        param_name=param_name,
        default_value=default_value,
        input_type=input_type,
        is_mandatory=is_mandatory,
        print_value=print_value,
    )


def init_manager(siemplify, integration_name, use_v2_manager=False):
    """
    Loads integration parameters and initiates ExchangeManager accordingly
    :param siemplify: {SiemplifyAction} Instance of the SiemplifyAction
    :param integration_name: {str} Name of the integration, which parameters should be extracted
    :return: {ExchangeManager} Instance of the ExchangeManager
    """
    manager = ExchangeManagerV2 if use_v2_manager else ExchangeManager
    # Load integration parameters
    server_address = extract_configuration_param(
        siemplify=siemplify,
        param_name="ServerAddress",
        is_mandatory=True,
        provider_name=integration_name,
    )
    domain = extract_configuration_param(
        siemplify=siemplify, param_name="Domain", provider_name=integration_name
    )
    username = extract_configuration_param(
        siemplify=siemplify,
        param_name="Username",
        is_mandatory=False,
        provider_name=integration_name,
    )
    password = extract_configuration_param(
        siemplify=siemplify,
        param_name="Password",
        is_mandatory=False,
        provider_name=integration_name,
    )
    mail_address = extract_configuration_param(
        siemplify=siemplify,
        param_name="Mail Address",
        is_mandatory=True,
        provider_name=integration_name,
    )
    use_domain = extract_configuration_param(
        siemplify=siemplify,
        param_name="Use Domain For Authentication",
        provider_name=integration_name,
        input_type=bool,
        default_value=True,
    )

    autodiscover = extract_configuration_param(
        siemplify=siemplify,
        param_name="Use Autodiscover Service",
        provider_name=integration_name,
        input_type=bool,
        default_value=False,
    )

    use_delegated_access = extract_configuration_param(
        siemplify=siemplify,
        param_name="Use Delegated Access",
        provider_name=integration_name,
        input_type=bool,
        default_value=False,
    )

    client_id = extract_configuration_param(
        siemplify=siemplify,
        param_name="Client ID",
        is_mandatory=False,
        provider_name=integration_name,
    )

    client_secret = extract_configuration_param(
        siemplify=siemplify,
        param_name="Client Secret",
        is_mandatory=False,
        provider_name=integration_name,
    )

    tenant_id = extract_configuration_param(
        siemplify=siemplify,
        param_name="Tenant (Directory) ID",
        is_mandatory=False,
        provider_name=integration_name,
    )

    redirect_url = extract_configuration_param(
        siemplify=siemplify,
        param_name="Redirect URL",
        is_mandatory=False,
        provider_name=integration_name,
    )

    refresh_token = extract_configuration_param(
        siemplify=siemplify,
        param_name="Refresh Token",
        is_mandatory=False,
        provider_name=integration_name,
    )

    base64_private_key = extract_configuration_param(
        siemplify=siemplify,
        param_name="Base64 Encoded Private Key",
        is_mandatory=False,
        provider_name=integration_name
    )

    base64_certificate = extract_configuration_param(
        siemplify=siemplify,
        param_name="Base64 Encoded Certificate",
        is_mandatory=False,
        provider_name=integration_name
    )

    base64_ca_certificate = extract_configuration_param(
        siemplify=siemplify,
        param_name="Base64 Encoded CA certificate",
        is_mandatory=False,
        provider_name=integration_name
    )

    verify_ssl = extract_configuration_param(
        siemplify=siemplify,
        param_name="Verify SSL",
        provider_name=integration_name,
        input_type=bool,
        default_value=False,
    )

    private_key_path, certificate_path, ca_certificate_path = None, None, None

    if base64_private_key:
        private_key_path = save_file_in_temp_folder(
            siemplify,
            base64_private_key,
            DECRYPT_PRIVATE_KEY_FILE_PATH,
            "Base64 Encoded Private Key"
        )
    if base64_certificate:
        certificate_path = save_file_in_temp_folder(
            siemplify,
            base64_certificate,
            DECRYPT_KEY_CERTIFICATE_FILE_PATH,
            "Base64 Encoded Certificate"
        )
    if base64_ca_certificate:
        ca_certificate_path = save_file_in_temp_folder(
            siemplify,
            base64_ca_certificate,
            DECRYPT_CA_CERTIFICATE_FILE_PATH,
            "Base64 Encoded CA certificate"
        )

    smime_auth = SmimeAuth(
        private_key_path=private_key_path,
        certificate_path=certificate_path,
        ca_certificate_path=ca_certificate_path,
        temp_folder_path=siemplify.get_temp_folder_path(),
    )

    return manager(
        exchange_server_ip=server_address,
        domain=domain,
        username=username,
        password=password,
        user_mail_address=mail_address,
        use_domain_in_auth=use_domain,
        autodiscover=autodiscover,
        use_delegated_access=use_delegated_access,
        siemplify_logger=siemplify.LOGGER,
        client_id=client_id,
        client_secret=client_secret,
        tenant_id=tenant_id,
        auth_token=refresh_token,
        redirect_url=redirect_url,
        verify_ssl=verify_ssl,
        smime_auth=smime_auth,
    )


def is_rtl(text):
    """
    Checks if presented text is bidirectional: https://en.wikipedia.org/wiki/Right-to-left_mark
    It's required for normal representation of such languages as Hebrew
    :param text: {unicode} Input text to check
    :return: {bool} True - if text is bidirectional; False - otherwise.
    """
    x = len([None for ch in text if bidirectional(ch) in ("R", "AL")]) / float(
        len(text)
    )
    return True if x > 0 else False


def add_rtl_html_divs_to_body(body):
    """
    Wraps entire text into HTML with direction marked as bidirectional.
    :param body: {str} Input text to wrap
    :return: {str} Text wrapped into <body> with dir='rtl' attribute
    """
    return f"<html><body dir='rtl'>{body}</body></html>"
