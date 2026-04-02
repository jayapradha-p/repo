from __future__ import annotations

import json

from TIPCommon.base.action import Action
from TIPCommon.extraction import extract_action_param, extract_configuration_param
from TIPCommon import validation
from TIPCommon.utils import is_empty_string_or_none
from TIPCommon.types import SingleJson

import consts
from datamodels import RemovedDataTableRow
from exceptions import GoogleChronicleValidationError, GoogleChronicleManagerError
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2
from utils import validate_api_root_for_backstory


class RemoveRowsFromDataTable(Action):

    def __init__(self) -> None:
        super().__init__(consts.REMOVE_ROWS_FROM_DATA_TABLE_SCRIPT_NAME)
        self.error_output_message = f"Error executing action \"{self.name}\"."
        self.output_message = ""
        self.result_value = False
        self.json_results: list[SingleJson] = []

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
        self.params.rows = extract_action_param(
            self.soar_action,
            param_name="Rows",
            print_value=True,
            is_mandatory=True,
        )
        self.params.rows_to_remove: list[SingleJson] = []

    def _validate_params(self) -> None:
        validate_api_root_for_backstory(self.params.api_root)
        validator = validation.ParameterValidator(self.soar_action)
        if not is_empty_string_or_none(self.params.user_service_account):
            self.params.user_service_account = validator.validate_json(
                param_name="User's Service Account",
                json_string=self.params.user_service_account,
                print_value=False,
            )
        self._parse_and_validate_rows_param()

    def _parse_and_validate_rows_param(self) -> None:
        try:
            parsed_rows = json.loads(self.params.rows)
            if not isinstance(parsed_rows, list):
                raise ValueError("Parameter 'Rows' must be a JSON list of objects.")
            for i, item in enumerate(parsed_rows):
                if not isinstance(item, dict):
                    raise ValueError(
                        f"Each item in 'Rows' (index {i}) must be a JSON object."
                    )
            self.params.rows_to_remove = parsed_rows
        except json.JSONDecodeError as e:
            raise GoogleChronicleValidationError(
                "invalid value provided in the “Rows” parameter. "
                "Please check the JSON payload."
            ) from e
        except ValueError as e:
            raise GoogleChronicleValidationError(str(e)) from e

    def _init_api_clients(self) -> GoogleChronicleManagerV2:
        return GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=self.params.user_service_account,
            chronicle_soar=self.soar_action,
            api_root=self.params.api_root,
            verify_ssl=self.params.verify_ssl,
            workload_identity_email=self.params.workload_identity_email,
        )

    def _perform_action(self, _=None) -> None:
        if not self.params.rows_to_remove:
            self._set_output_for_no_input_rows()
            return
        ordered_column_names = self._fetch_and_validate_table_schema()
        self._validate_input_rows_against_schema(ordered_column_names)
        matching_rows = self._find_rows_to_remove(ordered_column_names)
        removed_rows_data = self._call_remove_rows_api(matching_rows)
        self._process_api_response(removed_rows_data)

    def _set_output_for_no_input_rows(self) -> None:
        self.output_message = (
            f"No rows provided in the 'Rows' parameter to remove from "
            f"the data table '{self.params.data_table_name}'."
        )
        self.soar_action.LOGGER.info(self.output_message)
        self.result_value = True

    def _fetch_and_validate_table_schema(self) -> list[str]:
        table_details = self.api_client.data_table_details(
            self.params.data_table_name
        )
        if not table_details.column_info:
            raise GoogleChronicleValidationError(
                f"Data table '{self.params.data_table_name}' has no column info."
            )
        ordered_column_names = table_details.ordered_column_names
        if not ordered_column_names:
            raise GoogleChronicleValidationError(
                f"Data table '{self.params.data_table_name}' "
                "has no valid columns defined."
            )
        return ordered_column_names

    def _validate_input_rows_against_schema(
        self,
        ordered_column_names: list[str]
    ) -> None:
        valid_columns = set(col.lower() for col in ordered_column_names)
        for row_data_item in self.params.rows_to_remove:
            for key in row_data_item:
                if key.lower() not in valid_columns:
                    raise GoogleChronicleValidationError(
                        "invalid value provided in the \"Rows\" parameter. "
                        "Please check if the column names are correct."
                    )
        self.soar_action.LOGGER.info(
            f"All {len(self.params.rows_to_remove)} input rows "
            "passed schema validation."
        )

    def _find_rows_to_remove(self, ordered_column_names: list[str]) -> list[SingleJson]:
        column_index_map = {
            col.lower(): idx for idx, col in enumerate(ordered_column_names)
        }

        matched_rows = []
        seen_row_names = set()
        unmatched_queries = []

        for query in self.params.rows_to_remove:
            normalized_query = {
                c.lower(): str(v).strip().lower() for c, v in query.items()
            }
            _, filter_val = next(iter(normalized_query.items()))

            self.soar_action.LOGGER.info(
                f"Searching rows using server-side filter: '{filter_val}'"
            )

            found = False

            for row in self.api_client.list_all_data_table_rows(
                data_table_identifier=self.params.data_table_name,
                filter_query=filter_val,
            ):
                if row.name in seen_row_names:
                    continue

                is_match = True
                for col, expected_val in normalized_query.items():
                    idx = column_index_map.get(col)
                    if idx is None or idx >= len(row.values):
                        is_match = False
                        break

                    actual_val = str(row.values[idx]).strip().lower()
                    if actual_val != expected_val:
                        is_match = False
                        break

                if is_match:
                    matched_rows.append(row)
                    seen_row_names.add(row.name)
                    found = True
                    break

            if not found:
                unmatched_queries.append(query)

        if unmatched_queries:
            raise GoogleChronicleValidationError(
                "One or more input rows did not match any entries in data table "
                f'"{self.params.data_table_name}".'
            )

        self.soar_action.LOGGER.info(f"Matched {len(matched_rows)} row(s) for removal.")
        return matched_rows

    def _call_remove_rows_api(
        self,
        matching_rows: list[SingleJson]
    ) -> list[SingleJson]:
        removed_rows: list[SingleJson] = []
        for row in matching_rows:
            row_id = row.name.split("/")[-1]
            try:
                self.soar_action.LOGGER.info(
                    f"Attempting to delete row with ID: {row_id}"
                )
                self.api_client.delete_data_table_row(
                    self.params.data_table_name, row_id
                )
                removed_rows.append(row)
            except GoogleChronicleManagerError as e:
                self.soar_action.LOGGER.error(
                    f"Failed to remove row '{row_id}' due to API error: {str(e)}"
                )
        return removed_rows

    def _process_api_response(
        self,
        removed_rows_data: list[RemovedDataTableRow]
    ) -> None:
        count = len(removed_rows_data)
        if count > 0:
            self.result_value = True
            self.output_message = (
                "Successfully removed rows from the data table "
                f"\"{self.params.data_table_name}\" in Google SecOps."
            )
            self.json_results = self._build_json_results(removed_rows_data)
        else:
            self.result_value = False
            self.output_message = (
                "No rows were removed from the data table "
                f"\"{self.params.data_table_name}\". "
                "All rows may have failed to match or delete."
            )

    def _build_json_results(
        self,
        removed_rows_data: list[RemovedDataTableRow]
    ) -> list[SingleJson]:
        return [row.to_json() for row in removed_rows_data]

def main() -> None:
    RemoveRowsFromDataTable().run()

if __name__ == "__main__":
    main()
