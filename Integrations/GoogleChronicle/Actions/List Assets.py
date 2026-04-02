import datetime
from ScriptResult import (
    EXECUTION_STATE_COMPLETED,
    EXECUTION_STATE_FAILED,
    EXECUTION_STATE_TIMEDOUT,
)
from SiemplifyAction import SiemplifyAction
from SiemplifyDataModel import EntityTypes
from SiemplifyUtils import (
    convert_dict_to_json_result_dict,
    convert_unixtime_to_datetime,
    get_domain_from_entity,
    output_handler,
    unix_now,
)
from TIPCommon.extraction import extract_action_param, extract_configuration_param
from TIPCommon.transformation import construct_csv

import consts
import utils
from exceptions import InvalidTimeException
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2



SCRIPT_NAME = "List Assets"
SUPPORTED_ENTITIES = [EntityTypes.ADDRESS, EntityTypes.URL, EntityTypes.FILEHASH]


@output_handler
def main():
    siemplify = SiemplifyAction()
    siemplify.script_name = f"{consts.INTEGRATION_NAME} - {SCRIPT_NAME}"
    siemplify.LOGGER.info("================= Main - Param Init =================")

    # INIT INTEGRATION CONFIGURATION:
    creds = extract_configuration_param(
        siemplify,
        provider_name=consts.INTEGRATION_NAME,
        param_name="User's Service Account",
        remove_whitespaces=False,
    )
    workload_identity_email = extract_configuration_param(
        siemplify,
        provider_name=consts.INTEGRATION_NAME,
        param_name="Workload Identity Email",
    )
    api_root = extract_configuration_param(
        siemplify,
        provider_name=consts.INTEGRATION_NAME,
        param_name="API Root",
        is_mandatory=True,
        print_value=True,
    )
    verify_ssl = extract_configuration_param(
        siemplify,
        provider_name=consts.INTEGRATION_NAME,
        param_name="Verify SSL",
        is_mandatory=True,
        input_type=bool,
        print_value=True,
    )

    max_hours_backwards = extract_action_param(
        siemplify,
        param_name="Max Hours Backwards",
        is_mandatory=False,
        print_value=True,
        default_value=consts.MAX_HOURS_BACKWARDS,
        input_type=int,
    )
    limit = extract_action_param(
        siemplify,
        param_name="Max Assets To Return",
        is_mandatory=False,
        print_value=True,
        default_value=consts.LIMIT,
        input_type=int,
    )
    timeframe = extract_action_param(
        siemplify, param_name="Time Frame", is_mandatory=False, print_value=True
    )
    start_time_string = extract_action_param(
        siemplify, param_name="Start Time", is_mandatory=False, print_value=True
    )
    end_time_string = extract_action_param(
        siemplify, param_name="End Time", is_mandatory=False, print_value=True
    )

    if limit < 0:
        siemplify.LOGGER.info(
            '"Max Assets To Return" must be non-negative. Using default of'
            f" {consts.LIMIT}."
        )
        limit = consts.LIMIT

    if max_hours_backwards < 0:
        siemplify.LOGGER.info(
            '"Max Hours Backwards" must be non-negative. Using default of'
            f" {consts.MAX_HOURS_BACKWARDS}."
        )
        max_hours_backwards = consts.MAX_HOURS_BACKWARDS

    siemplify.LOGGER.info("----------------- Main - Started -----------------")

    status = EXECUTION_STATE_COMPLETED
    successful_entities = []
    missing_entities = []
    failed_entities = []
    json_results = {}
    output_message = ""
    result_value = "false"

    try:
        manager = GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=creds,
            chronicle_soar=siemplify,
            api_root=api_root,
            verify_ssl=verify_ssl,
            workload_identity_email=workload_identity_email,
        )

        if timeframe == consts.HOURS_BACKWARDS_STRING:
            end_time = datetime.datetime.utcnow()
            start_time = end_time - datetime.timedelta(hours=max_hours_backwards)

            # Convert to RFC 3339
            end_time = utils.datetime_to_rfc3339(end_time)
            start_time = utils.datetime_to_rfc3339(start_time)
        else:
            start_time, end_time = utils.get_timestamps(
                timeframe, start_time_string, end_time_string
            )

        for entity in siemplify.target_entities:
            if unix_now() >= siemplify.execution_deadline_unix_time_ms:
                siemplify.LOGGER.error(
                    "Timed out. execution deadline "
                    f"({convert_unixtime_to_datetime(siemplify.execution_deadline_unix_time_ms)}) "
                    "has passed."
                )
                status = EXECUTION_STATE_TIMEDOUT
                break

            try:
                if entity.entity_type not in SUPPORTED_ENTITIES:
                    siemplify.LOGGER.info(
                        f"Entity {entity.identifier} is of unsupported type. "
                        "Skipping."
                    )
                    continue

                siemplify.LOGGER.info(f"Started processing entity: {entity.identifier}")
                siemplify.LOGGER.info(f"Fetching assets for {entity.identifier}")

                assets = []
                uri = []

                if entity.entity_type == EntityTypes.ADDRESS:
                    uri, assets = manager.list_assets(
                        start_time=start_time,
                        end_time=end_time,
                        ip=entity.identifier,
                        limit=limit,
                    )
                    if not uri:
                        uri = [
                            utils.construct_url(
                                consts.LIST_ASSETS_IP_URI,
                                siemplify.platform_url,
                                entity.identifier,
                                consts.ENTITY_TYPE_TO_ASSET_TYPE_MAPPING.get(
                                    entity.entity_type
                                ),
                                params={"referenceTime": end_time}
                            )
                        ]

                elif entity.entity_type == EntityTypes.URL:
                    domain = get_domain_from_entity(entity)
                    uri, assets = manager.list_assets(
                        start_time=start_time,
                        end_time=end_time,
                        domain=domain,
                        limit=limit,
                    )
                    if not uri:
                        uri = [
                            utils.construct_url(
                                consts.LIST_ASSETS_DOMAIN_URI,
                                siemplify.platform_url,
                                domain,
                                consts.ENTITY_TYPE_TO_ASSET_TYPE_MAPPING.get(
                                    entity.entity_type
                                ),
                                params={"whoIsTimestamp": end_time}
                            )
                        ]

                elif entity.entity_type == EntityTypes.FILEHASH:
                    if len(entity.identifier) not in [
                        consts.SHA256_LENGTH,
                        consts.MD5_LENGTH,
                        consts.SHA1_LENGTH,
                    ]:
                        siemplify.LOGGER.error(
                            "Not supported hash type. Provide either MD5,"
                            " SHA-256 or SHA-1."
                        )
                        siemplify.LOGGER.info(
                            f"Finished processing entity {entity.identifier}"
                        )
                        continue
                    uri, assets = manager.list_assets(
                        start_time=start_time,
                        end_time=end_time,
                        file_hash=entity.identifier,
                        limit=limit,
                    )
                    if not uri:
                        uri = [
                            utils.construct_url(
                                consts.LIST_ASSETS_HASH_URI,
                                siemplify.platform_url,
                                entity.identifier,
                                consts.ENTITY_TYPE_TO_ASSET_TYPE_MAPPING.get(
                                    utils.get_hash_type(entity.identifier)
                                ),
                                params={
                                    "startTime": start_time,
                                    "endTime": end_time,
                                    "referenceTime": end_time,
                                }
                            )
                        ]

                siemplify.LOGGER.info(
                    f"Found {len(assets)} assets for {entity.identifier}"
                )

                json_results[entity.identifier] = {
                    "assets": [asset.raw_data for asset in assets],
                    "uri": uri,
                }

                if assets:
                    siemplify.result.add_entity_table(
                        entity.identifier,
                        construct_csv([asset.as_csv() for asset in assets]),
                    )
                    successful_entities.append(entity)

                else:
                    missing_entities.append(entity)
                siemplify.LOGGER.info(f"Finished processing entity {entity.identifier}")

            except Exception as e:
                failed_entities.append(entity)
                siemplify.LOGGER.error(
                    f"An error occurred on entity {entity.identifier}"
                )
                siemplify.LOGGER.exception(e)

        if successful_entities:
            output_message += (
                "Successfully listed related assets for the following entities"
                " from Google Chronicle:\n   {}\n\n".format(
                    "\n   ".join([entity.identifier for entity in successful_entities])
                )
            )
            siemplify.update_entities(successful_entities)
            result_value = "true"

        if missing_entities:
            output_message += (
                "No related assets were found for the following entities from"
                " Google Chronicle:\n   {}\n\n".format(
                    "\n   ".join([entity.identifier for entity in missing_entities])
                )
            )
            result_value = "true"

        if not successful_entities and not missing_entities:
            output_message += "No assets were found for the provided entities.\n\n"

        if failed_entities:
            output_message += (
                "Action was not able to list related assets for the following"
                " entities from Google Chronicle:\n   {}".format(
                    "\n   ".join([entity.identifier for entity in failed_entities])
                )
            )

    except InvalidTimeException:
        result_value = False
        status = EXECUTION_STATE_FAILED
        output_message = (
            f'Error executing action "{SCRIPT_NAME}". Reason: "Start Time"'
            ' should be provided, when "Custom" is selected in "Time Frame"'
            " parameter."
        )

    except Exception as e:
        siemplify.LOGGER.error(f'Error executing action "{SCRIPT_NAME}". Reason: {e}')
        siemplify.LOGGER.exception(e)
        status = EXECUTION_STATE_FAILED
        result_value = "false"
        output_message = f'Error executing action "{SCRIPT_NAME}". Reason: {e}'

    siemplify.result.add_result_json(convert_dict_to_json_result_dict(json_results))
    siemplify.LOGGER.info("----------------- Main - Finished -----------------")
    siemplify.LOGGER.info(f"Status: {status}")
    siemplify.LOGGER.info(f"Result Value: {result_value}")
    siemplify.LOGGER.info(f"Output Message: {output_message}")
    siemplify.end(output_message, result_value, status)


if __name__ == "__main__":
    main()
