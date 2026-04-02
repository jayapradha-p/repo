import sys

from EnvironmentCommon import GetEnvironmentCommonFactory
from SiemplifyConnectors import SiemplifyConnectorExecution
from SiemplifyUtils import output_handler, unix_now
from TIPCommon.extraction import extract_connector_param
from TIPCommon.utils import is_overflowed

from consts import (
    ALERT_TYPES,
    ALERT_TYPE_NAMES,
    FALLBACK_SEVERITY_VALUES,
    UNIFIED_CONNECTOR_CONNECTOR_NAME,
    UNIFIED_CONNECTOR_DEFAULT_LIMIT,
    UNIFIED_CONNECTOR_DEFAULT_TIME_FRAME,
    UNIFIED_CONNECTOR_MAX_TIME_FRAME,
)
from exceptions import GoogleChronicleValidationError
from ExternalAlert import ExternalAlert
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2
from IOCAlert import IOCAlert
from RuleAlert import RuleAlert
from utils import convert_list_to_comma_string, is_approaching_timeout


ALERT_TYPE_OBJECTS = {
    ALERT_TYPES.get("rule"): RuleAlert,
    ALERT_TYPES.get("external"): ExternalAlert,
    ALERT_TYPES.get("ioc"): IOCAlert,
}


connector_starting_time = unix_now()


@output_handler
def main(is_test_run):
    siemplify = SiemplifyConnectorExecution()
    siemplify.script_name = UNIFIED_CONNECTOR_CONNECTOR_NAME
    processed_alerts = []

    if is_test_run:
        siemplify.LOGGER.info(
            '***** This is an "IDE Play Button"\\"Run Connector once" test run ******'
        )

    siemplify.LOGGER.info("------------------- Main - Param Init -------------------")

    api_root = extract_connector_param(
        siemplify, param_name="API Root", is_mandatory=True, print_value=True
    )
    users_service_account = extract_connector_param(
        siemplify, param_name="User's Service Account", is_mandatory=False
    )
    workload_identity_email = extract_connector_param(
        siemplify, param_name="Workload Identity Email", print_value=False
    )
    verify_ssl = extract_connector_param(
        siemplify,
        param_name="Verify SSL",
        input_type=bool,
        is_mandatory=True,
        print_value=True,
    )
    environment_field_name = extract_connector_param(
        siemplify, param_name="Environment Field Name", print_value=True
    )
    environment_regex_pattern = extract_connector_param(
        siemplify, param_name="Environment Regex Pattern", print_value=True
    )
    script_timeout = extract_connector_param(
        siemplify,
        param_name="PythonProcessTimeout",
        is_mandatory=True,
        input_type=int,
        print_value=True,
    )
    hours_backwards = extract_connector_param(
        siemplify,
        param_name="Max Hours Backwards",
        input_type=int,
        default_value=UNIFIED_CONNECTOR_DEFAULT_TIME_FRAME,
        print_value=True,
    )
    fetch_limit = extract_connector_param(
        siemplify,
        param_name="Max Alerts To Fetch",
        input_type=int,
        default_value=UNIFIED_CONNECTOR_DEFAULT_LIMIT,
        print_value=True,
    )
    fallback_severity = extract_connector_param(
        siemplify, param_name="Fallback Severity", is_mandatory=True, print_value=True
    )
    device_product_field = extract_connector_param(
        siemplify, param_name="DeviceProductField", is_mandatory=True
    )
    disable_overflow = extract_connector_param(
        siemplify,
        param_name="Disable Overflow",
        input_type=bool,
        default_value=False,
        print_value=True,
    )

    alert_types = [ALERT_TYPES.get("rule")]

    try:
        siemplify.LOGGER.info("------------------- Main - Started -------------------")

        if not all(alert_type in ALERT_TYPES.values() for alert_type in alert_types):
            raise GoogleChronicleValidationError(
                f'Invalid value provided for "Alert Types". Possible values: '
                f"{convert_list_to_comma_string(list(ALERT_TYPE_NAMES.values()))}"
            )

        if fallback_severity.lower() not in FALLBACK_SEVERITY_VALUES:
            raise GoogleChronicleValidationError(
                f'Invalid value provided for the parameter "Fallback Severity": {fallback_severity}. '
                f"Possible values: {convert_list_to_comma_string(FALLBACK_SEVERITY_VALUES)}."
            )

        if fetch_limit < 0:
            siemplify.LOGGER.info(
                f'"Max Alerts To Fetch" must be non-negative. The default value '
                f"{UNIFIED_CONNECTOR_DEFAULT_LIMIT} will be used"
            )
            fetch_limit = UNIFIED_CONNECTOR_DEFAULT_LIMIT

        if hours_backwards < 0:
            siemplify.LOGGER.info(
                f'"Max Hours Backwards" must be non-negative. The default value '
                f"{UNIFIED_CONNECTOR_DEFAULT_TIME_FRAME} will be used"
            )
            hours_backwards = UNIFIED_CONNECTOR_DEFAULT_TIME_FRAME

        if hours_backwards > UNIFIED_CONNECTOR_MAX_TIME_FRAME:
            siemplify.LOGGER.info(
                f'"Max Hours Backwards" is greater than maximum allowed value. The maximum value '
                f"{UNIFIED_CONNECTOR_MAX_TIME_FRAME} will be used"
            )
            hours_backwards = UNIFIED_CONNECTOR_MAX_TIME_FRAME

        # if padding_period is not None and (padding_period < 0 or padding_period > MAX_PADDING_PERIOD):
        #     siemplify.LOGGER.info(f"\"Padding Period\" must be non-negative and maximum is 12 hours. The default value "
        #                           f"{DEFAULT_PADDING_PERIOD} will be used")
        #     padding_period = DEFAULT_PADDING_PERIOD

        manager = GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=users_service_account,
            workload_identity_email=workload_identity_email,
            chronicle_soar=siemplify,
            api_root=api_root,
            verify_ssl=verify_ssl,
        )

        for alert_type in alert_types:
            siemplify.LOGGER.info(
                f"Started processing {ALERT_TYPE_NAMES.get(alert_type)} alert type"
            )

            if is_approaching_timeout(script_timeout, connector_starting_time):
                siemplify.LOGGER.info(
                    "Timeout is approaching. Connector will gracefully exit"
                )
                break

            alert_type_processed_alerts = []
            fetched_alerts = []
            alert_object = ALERT_TYPE_OBJECTS.get(alert_type)(
                siemplify, manager, script_timeout, connector_starting_time
            )

            # Read already existing alerts ids
            existing_ids = alert_object.read_ids()

            # Fetch alerts
            filtered_alerts = alert_object.get_alerts(
                existing_ids=existing_ids,
                fetch_limit=fetch_limit,
                hours_backwards=hours_backwards,
                fallback_severity=fallback_severity,
            )

            for alert in filtered_alerts:
                try:
                    if is_approaching_timeout(script_timeout, connector_starting_time):
                        siemplify.LOGGER.info(
                            "Timeout is approaching. Connector will gracefully exit"
                        )
                        break

                    siemplify.LOGGER.info(
                        f"Started processing {ALERT_TYPE_NAMES.get(alert_type)} alert {alert.id}"
                    )
                    if is_test_run and alert_type_processed_alerts:
                        siemplify.LOGGER.info(
                            "This is a TEST run. "
                            f"Only 1 {ALERT_TYPE_NAMES.get(alert_type)} alert will be "
                            "processed."
                        )
                        alert_type_processed_alerts = alert_type_processed_alerts[:1]
                        break
                    existing_ids.append(alert.id)
                    fetched_alerts.append(alert)

                    if not alert_object.pass_filters(alert):
                        continue

                    alert_info = alert_object.get_alert_info(
                        alert,
                        GetEnvironmentCommonFactory().create_environment_manager(
                            siemplify,
                            environment_field_name,
                            environment_regex_pattern,
                        ),
                        device_product_field,
                    )

                    if not disable_overflow:
                        if is_overflowed(siemplify, alert_info, is_test_run):
                            siemplify.LOGGER.info(
                                f"{str(alert_info.rule_generator)}"
                                f"-{str(alert_info.ticket_id)}"
                                f"-{str(alert_info.environment)}"
                                f"-{str(alert_info.device_product)} "
                                "found as overflow alert. Skipping..."
                            )
                            # If is overflowed we should skip
                            continue

                    alert_type_processed_alerts.append(alert_info)
                    siemplify.LOGGER.info(
                        f"{ALERT_TYPE_NAMES.get(alert_type)} alert {alert.id} was created."
                    )

                except Exception as e:
                    siemplify.LOGGER.error(
                        f"Failed to process {ALERT_TYPE_NAMES.get(alert_type)} alert {alert.id}"
                    )
                    siemplify.LOGGER.exception(e)

                    if is_test_run:
                        raise

                siemplify.LOGGER.info(
                    f"Finished processing {ALERT_TYPE_NAMES.get(alert_type)} alert {alert.id}"
                )

            else:
                if not is_test_run:
                    siemplify.LOGGER.info(
                        f"Saving {ALERT_TYPE_NAMES.get(alert_type)} timestamp."
                    )
                    alert_object.save_timestamp(fetched_alerts)

            if not is_test_run:
                siemplify.LOGGER.info(
                    f"Saving {ALERT_TYPE_NAMES.get(alert_type)} existing ids."
                )
                alert_object.write_ids(list(set(existing_ids)))

            processed_alerts.extend(alert_type_processed_alerts)
            siemplify.LOGGER.info(
                f"Processed {len(alert_type_processed_alerts)} "
                f"{ALERT_TYPE_NAMES.get(alert_type)} alerts"
            )

    except Exception as e:
        siemplify.LOGGER.error(f"Got exception on main handler. Error: {e}")
        siemplify.LOGGER.exception(e)

        if is_test_run:
            raise

    siemplify.LOGGER.info(f"Created total of {len(processed_alerts)} cases")
    siemplify.LOGGER.info("------------------- Main - Finished -------------------")
    siemplify.return_package(processed_alerts)


if __name__ == "__main__":
    # Connectors are run in iterations. The interval is configurable from the ConnectorsScreen UI.
    is_test = not (len(sys.argv) < 2 or sys.argv[1] == "True")
    main(is_test)
