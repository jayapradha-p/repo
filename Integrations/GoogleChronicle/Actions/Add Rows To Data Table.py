from __future__ import annotations

import json
from typing import Any

from TIPCommon.base.action import Action
from TIPCommon.extraction import extract_action_param, extract_configuration_param
from TIPCommon import validation
from TIPCommon.utils import is_empty_string_or_none
from TIPCommon.types import SingleJson

import consts
from exceptions import (
    GoogleChronicleManagerError,
    GoogleChronicleValidationError,
)
from datamodels import AddedDataTableRow, DataTableDetails
from GoogleChronicleManager import (
    GoogleChronicleManager,
)
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2
from utils import validate_api_root_for_backstory


class AddRowsToDataTableAction(Action):

    def __init__(self) -> None:
        super().__init__(consts.ADD_ROWS_TO_DATA_TABLE_SCRIPT_NAME)
        self.output_message: str = ""
        self.json_results: SingleJson = {}

    def _extract_action_parameters(self) -> None:
        self.params.user_service_account = extract_configuration_param(
            self.soar_action,
            provider_name=consts.INTEGRATION_NAME,
            param_name="User's Service Account",
            remove_whitespaces=False,
        )
        self.params.workload_identity_email = extract_configuration_param(
            self.soar_action,
            provider_name=consts.INTEGRATION_NAME,
            param_name="Workload Identity Email",
        )

        self.params.api_root = extract_configuration_param(
            self.soar_action,
            provider_name=consts.INTEGRATION_NAME,
            param_name="API Root",
            is_mandatory=True,
            print_value=True,
        )

        self.params.verify_ssl = extract_configuration_param(
            self.soar_action,
            provider_name=consts.INTEGRATION_NAME,
            param_name="Verify SSL",
            is_mandatory=True,
            input_type=bool,
            print_value=True,
        )

        self.params.data_table_name = extract_action_param(
            self.soar_action,
            param_name="Data Table Name",
            print_value=True,
            is_mandatory=True,
        )

        self.params.rows_json_string = extract_action_param(
            self.soar_action,
            param_name="Rows",
            print_value=True,
            is_mandatory=True,
        )

        self.params.rows_to_add: list[SingleJson] = []

    def _validate_params(self) -> None:
        validator = validation.ParameterValidator(self.soar_action)
        if not is_empty_string_or_none(self.params.user_service_account):
            self.params.user_service_account = validator.validate_json(
                param_name="User's Service Account",
                json_string=self.params.user_service_account,
                print_value=False,
            )
        validate_api_root_for_backstory(self.params.api_root)
        parsed_rows = self._parse_rows_json()
        self._validate_rows_list(parsed_rows)
        self._validate_each_row(parsed_rows)
        self.params.rows_to_add = parsed_rows

    def _init_api_clients(self) -> GoogleChronicleManager:
        return GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=self.params.user_service_account,
            chronicle_soar=self.soar_action,
            api_root=self.params.api_root,
            verify_ssl=self.params.verify_ssl,
            workload_identity_email=self.params.workload_identity_email,
        )

    def _perform_action(self, _=None) -> None:
        ordered_column_names, parent_resource_name = (
            self._fetch_and_validate_table_schema()
        )
        self._validate_input_rows_against_schema(ordered_column_names)

        api_payloads = self._prepare_api_payloads(ordered_column_names)

        added_rows_data = self._call_add_rows_api(parent_resource_name, api_payloads)
        self._process_api_response(added_rows_data)

    def _parse_rows_json(self) -> Any:
        try:
            return json.loads(self.params.rows_json_string)
        except json.JSONDecodeError as e:
            raise GoogleChronicleValidationError(
                "Invalid value provided in the \"Rows\" parameter. "
                "Please check the JSON payload."
            ) from e

    def _validate_rows_list(self, parsed_rows: Any) -> None:
        if not isinstance(parsed_rows, list):
            raise GoogleChronicleValidationError(
                f"Parameter \"{consts.PARAM_ROWS}\" must be a JSON list of objects."
            )

    def _validate_each_row(self, parsed_rows: list) -> None:
        for i, item in enumerate(parsed_rows):
            if not isinstance(item, dict):
                raise GoogleChronicleValidationError(
                    "Each item in the arameter "
                    f"(at index {i}) must be a JSON object."
                )

    def _fetch_and_validate_table_schema(self) -> tuple[list[str], str]:
        table_details = self._fetch_table_details()
        return self._extract_and_validate_schema_from_details(table_details)

    def _fetch_table_details(self) -> DataTableDetails:
        self.soar_action.LOGGER.info(
            f"Fetching details for data table: {self.params.data_table_name}"
        )
        try:
            table_details = self.api_client.data_table_details(
                data_table_identifier=self.params.data_table_name
            )
        except GoogleChronicleManagerError as exc:
            raise GoogleChronicleManagerError(
                "Failed to fetch details for data table "
                f"\"{self.params.data_table_name}\". "
                "The table might not exist or an API error occurred."
            ) from exc

        return table_details

    def _extract_and_validate_schema_from_details(
        self,
        table_details: DataTableDetails,
    ) -> tuple[list[str], str]:
        self._validate_table_details_response(table_details)
        ordered_column_names = self._extract_ordered_columns(table_details)
        parent_resource_name = table_details.name

        self.soar_action.LOGGER.info(
            f"Data table schema columns (ordered): {', '.join(ordered_column_names)}."
        )

        return ordered_column_names, parent_resource_name

    def _validate_table_details_response(self, table_details: DataTableDetails) -> None:
        if not table_details.column_info:
            raw_data_json = json.dumps(table_details.raw_data)
            error_message = (
                f"Data table \"{self.params.data_table_name}\" does not have "
                "'columnInfo' or 'columnInfo' is empty. "
                f"API Response: {raw_data_json}"
            )
            raise GoogleChronicleValidationError(error_message)

        if table_details.name is None:
            raw_data_json = json.dumps(table_details.raw_data)
            error_message = (
                f"Data table \"{self.params.data_table_name}\" details response is "
                "missing the 'name' (parent resource name). "
                f"API Response: {raw_data_json}"
            )
            raise GoogleChronicleValidationError(error_message)

    def _extract_ordered_columns(self, table_details: DataTableDetails) -> list[str]:
        ordered_column_names = table_details.ordered_column_names
        if not ordered_column_names:
            raise GoogleChronicleValidationError(
                f"Data table \"{self.params.data_table_name}\" has no columns "
                "defined with 'originalColumn' in 'columnInfo'."
            )
        return ordered_column_names

    def _validate_input_rows_against_schema(
        self,
        ordered_column_names: list[str],
    ) -> None:
        for _i, row_data_item in enumerate(self.params.rows_to_add):
            missing_keys = [
                col_name
                for col_name in ordered_column_names
                if col_name not in row_data_item
            ]
            if missing_keys:
                raise GoogleChronicleValidationError(
                    "invalid value provided in the \"Rows\" parameter. Please check "
                    "if the column names are correct."
                )

        self.soar_action.LOGGER.info(
            f"All {len(self.params.rows_to_add)} provided rows passed "
            "column validation against table schema."
        )

    def _prepare_api_payloads(
        self,
        ordered_column_names: list[str],
    ) -> list[SingleJson]:
        all_row_payloads_for_api: list[SingleJson] = []
        for row_data_item in self.params.rows_to_add:
            payload_values = [
                str(row_data_item[col_name])
                if row_data_item.get(col_name) is not None
                else ""
                for col_name in ordered_column_names
            ]
            all_row_payloads_for_api.append({"values": payload_values})
        return all_row_payloads_for_api

    def _call_add_rows_api(
        self,
        parent_resource_name: str,
        all_row_payloads_for_api: list[SingleJson],
    ) -> list[AddedDataTableRow]:
        self.soar_action.LOGGER.info(
            f"Attempting to add {len(all_row_payloads_for_api)} row(s) "
            f"in bulk to data table \"{self.params.data_table_name}\"."
        )
        if all_row_payloads_for_api:
            self.soar_action.LOGGER.info(
                "Sample of first row payload for bulk add: "
                f"{json.dumps(all_row_payloads_for_api[0])}"
            )
        try:
            added_rows_data: list[AddedDataTableRow] = (
                self.api_client.add_rows_to_data_table(
                    data_table_identifier=self.params.data_table_name,
                    parent_resource_name=parent_resource_name,
                    individual_row_values_list=all_row_payloads_for_api,
                )
            )
        except GoogleChronicleManagerError as req_e:
            raise GoogleChronicleManagerError(
                "Network error during bulk add to data table "
                f"'{self.params.data_table_name}': {req_e}"
            ) from req_e

        self.soar_action.LOGGER.info(
            "Successfully submitted bulk request. API reported "
            f"{len(added_rows_data)} row(s) added."
        )
        if added_rows_data:
            self.soar_action.LOGGER.info(
                "Sample of first added row data from API: "
                f"{json.dumps(added_rows_data[0].to_json())}"
            )

        return added_rows_data

    def _process_api_response(
        self,
        added_rows_api_data: list[AddedDataTableRow],
    ) -> None:
        successfully_added_count = len(added_rows_api_data)

        if successfully_added_count > 0:
            self.output_message = (
                "Successfully added rows to the data table "
                f"\"{self.params.data_table_name}\" in Google SecOps."
            )
            self.json_results = self._build_json_results(added_rows_api_data)
        else:
            if self.params.rows_to_add:
                self.output_message = (
                    "Failed to add rows to data table "
                    f"\"{self.params.data_table_name}\". "
                    "The operation completed but no rows were reported as added. "
                    "Check API response and logs."
                )

    def _build_json_results(
        self,
        added_rows_api_data: list[AddedDataTableRow],
    ) -> list[SingleJson]:
        if len(added_rows_api_data) == len(self.params.rows_to_add):
            processed_results: list[SingleJson] = []
            for i, api_row_object in enumerate(added_rows_api_data):
                api_response_for_row = api_row_object.to_json()
                original_input_row_dict = self.params.rows_to_add[i]
                transformed_row = {
                    "name": api_response_for_row.get("name"),
                    "values": original_input_row_dict,
                }
                processed_results.append(transformed_row)
            return processed_results

        return [row.to_json() for row in added_rows_api_data]


def main() -> None:
    action = AddRowsToDataTableAction()
    action.run()


if __name__ == "__main__":
    main()
