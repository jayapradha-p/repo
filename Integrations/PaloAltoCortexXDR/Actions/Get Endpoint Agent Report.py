from SiemplifyAction import SiemplifyAction
from SiemplifyDataModel import EntityTypes
from SiemplifyUtils import (
    unix_now,
    convert_unixtime_to_datetime,
    output_handler,
    convert_dict_to_json_result_dict,
    flat_dict_to_csv,
)
from ScriptResult import (
    EXECUTION_STATE_COMPLETED,
    EXECUTION_STATE_FAILED,
    EXECUTION_STATE_TIMEDOUT,
)
from action_init import create_api_client
from constants import INTEGRATION_NAME, GET_ENDPOINT_AGENT_REPORT_ACTION_SCRIPT_NAME
from exceptions import XDRNotFoundException


SUPPORTED_ENTITIES = [EntityTypes.ADDRESS, EntityTypes.HOSTNAME]


@output_handler
def main():
    siemplify = SiemplifyAction()
    siemplify.script_name = (
        f"{INTEGRATION_NAME} - {GET_ENDPOINT_AGENT_REPORT_ACTION_SCRIPT_NAME}"
    )
    siemplify.LOGGER.info("================= Main - Param Init =================")
    siemplify.LOGGER.info("----------------- Main - Started -----------------")

    status = EXECUTION_STATE_COMPLETED
    successful_entities = []
    missing_entities = []
    json_results = {}
    failed_entities = []
    output_message = ""
    result_value = "true"

    try:
        xdr_manager = create_api_client(siemplify)

        for entity in siemplify.target_entities:
            if unix_now() >= siemplify.execution_deadline_unix_time_ms:
                siemplify.LOGGER.error(
                    f"Timed out. execution deadline ({convert_unixtime_to_datetime(siemplify.execution_deadline_unix_time_ms)}) has passed"
                )
                status = EXECUTION_STATE_TIMEDOUT
                break

            try:
                if entity.entity_type not in SUPPORTED_ENTITIES:
                    siemplify.LOGGER.info(
                        f"Entity {entity.identifier} is of unsupported type. Skipping."
                    )
                    continue

                siemplify.LOGGER.info(f"Started processing entity: {entity.identifier}")
                endpoint = None

                if entity.entity_type == EntityTypes.HOSTNAME:
                    try:
                        siemplify.LOGGER.info(
                            f"Fetching endpoint for hostname {entity.identifier}"
                        )
                        endpoint = xdr_manager.get_endpoint_by_hostname(
                            entity.identifier
                        )
                    except XDRNotFoundException as e:
                        # Endpoint was not found in Cortex XDR - skip entity
                        missing_entities.append(entity)
                        siemplify.LOGGER.info(str(e))
                        siemplify.LOGGER.info(f"Skipping entity {entity.identifier}")
                        continue

                if entity.entity_type == EntityTypes.ADDRESS:
                    try:
                        siemplify.LOGGER.info(
                            f"Fetching endpoint for address {entity.identifier}"
                        )
                        endpoint = xdr_manager.get_endpoint_by_ip(entity.identifier)
                    except XDRNotFoundException as e:
                        # Endpoint was not found in Cortex XDR - skip entity
                        missing_entities.append(entity)
                        siemplify.LOGGER.info(str(e))
                        siemplify.LOGGER.info(f"Skipping entity {entity.identifier}")
                        continue

                agent_report = xdr_manager.get_endpoint_agent_report(
                    endpoint.endpoint_id
                )

                json_results[entity.identifier] = agent_report.raw_data
                siemplify.result.add_entity_table(
                    f"Entity {entity.identifier} agent report found",
                    flat_dict_to_csv(agent_report.as_csv()),
                )
                entity.is_enriched = True

                successful_entities.append(entity)
                siemplify.LOGGER.info(f"Finished processing entity {entity.identifier}")

            except Exception as e:
                failed_entities.append(entity)
                siemplify.LOGGER.error(
                    f"An error occurred on entity {entity.identifier}"
                )
                siemplify.LOGGER.exception(e)

        if successful_entities:
            output_message += "Successfully fetched agent report for the following entities:\n   {}".format(
                "\n   ".join([entity.identifier for entity in successful_entities])
            )
            siemplify.update_entities(successful_entities)
        else:
            output_message += "No entities were processed."

        if missing_entities:
            output_message += "\n\nAction was not able to find endpoints matching the following entities:\n   {}".format(
                "\n   ".join([entity.identifier for entity in missing_entities])
            )

        if failed_entities:
            output_message += (
                "\n\nFailed processing the following entities:\n   {}".format(
                    "\n   ".join([entity.identifier for entity in failed_entities])
                )
            )

    except Exception as e:
        siemplify.LOGGER.error(f"Action didn't complete due to error: {e}")
        siemplify.LOGGER.exception(e)
        status = EXECUTION_STATE_FAILED
        result_value = "false"
        output_message = f"Action didn't complete due to error: {e}"

    siemplify.result.add_result_json(convert_dict_to_json_result_dict(json_results))
    siemplify.LOGGER.info("----------------- Main - Finished -----------------")
    siemplify.LOGGER.info(f"Status: {status}:")
    siemplify.LOGGER.info(f"Result Value: {result_value}")
    siemplify.LOGGER.info(f"Output Message: {output_message}")
    siemplify.end(output_message, result_value, status)


if __name__ == "__main__":
    main()
