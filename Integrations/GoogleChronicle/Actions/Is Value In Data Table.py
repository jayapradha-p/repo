from __future__ import annotations

from typing import Iterator

import json

from TIPCommon.base.action import Action
from TIPCommon.extraction import extract_action_param, extract_configuration_param
from TIPCommon.transformation import string_to_multi_value
from TIPCommon.validation import ParameterValidator
from TIPCommon.utils import is_empty_string_or_none
from TIPCommon.types import SingleJson

import consts
from exceptions import (
    GoogleChronicleAPILimitError,
    GoogleChronicleManagerError,
    GoogleChronicleValidationError,
)
from datamodels import AddedDataTableRow, DataTableDetails
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2
from utils import validate_api_root_for_backstory


class IsValueInDataTableAction(Action):

    def __init__(self) -> None:
        super().__init__(consts.IS_VALUE_IN_DATA_TABLE_SCRIPT_NAME)
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
        self.params.column_data_str = extract_action_param(
            self.soar_action,
            param_name="Column",
            print_value=True,
            is_mandatory=False,
        )
        self.params.values_data_str = extract_action_param(
            self.soar_action,
            param_name="Values",
            print_value=True,
            is_mandatory=True,
        )
        self.params.case_insensitive_search = extract_action_param(
            self.soar_action,
            param_name="Case Insensitive Search",
            print_value=True,
            is_mandatory=False,
            input_type=bool,
            default_value=True,
        )
        self.params.max_data_table_rows_to_return = extract_action_param(
            self.soar_action,
            param_name="Max Data Table Rows To Return",
            print_value=True,
            is_mandatory=True,
            input_type=int,
            default_value=consts.MAX_DATA_TABLE_ROWS_TO_RETURN,
        )
        self.params.columns_to_search: list[str] = []
        self.params.values_to_search: list[str] = []

    def _validate_params(self) -> None:
        validator = ParameterValidator(self.soar_action)
        if not is_empty_string_or_none(self.params.user_service_account):
            self.params.user_service_account = validator.validate_json(
                param_name="User's Service Account",
                json_string=self.params.user_service_account,
                print_value=False,
            )

        validator.validate_range(
            param_name="Max Data Table Rows To Return",
            value=self.params.max_data_table_rows_to_return,
            min_limit=consts.MINIMUM_DATA_TABLE_ROWS_TO_RETURN,
            max_limit=consts.MAX_DATA_TABLE_ROWS_TO_RETURN,
        )

        if not self.params.values_data_str or not self.params.values_data_str.strip():
            raise GoogleChronicleValidationError(
                'Parameter "Values" is mandatory and cannot be empty.'
            )
        self.params.values_to_search: list[str] = string_to_multi_value(
            string_value=self.params.values_data_str,
        )
        if not self.params.values_to_search:
            raise GoogleChronicleValidationError(
                'Parameter "Values" is mandatory and cannot be empty.'
            )

        if self.params.column_data_str and self.params.column_data_str.strip():
            self.params.columns_to_search: list[str] = string_to_multi_value(
                string_value=self.params.column_data_str,
            )

    def _init_api_clients(self) -> GoogleChronicleManagerV2:
        return GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=self.params.user_service_account,
            chronicle_soar=self.soar_action,
            api_root=self.params.api_root,
            verify_ssl=self.params.verify_ssl,
            workload_identity_email=self.params.workload_identity_email,
        )

    def _perform_action(self, _=None) -> None:
        validate_api_root_for_backstory(self.params.api_root)

        ordered_columns, columns_to_search = self._get_search_configuration()
        all_results, found_any = self._process_value_searches(
            ordered_columns, columns_to_search
        )
        self._set_final_output(all_results, found_any)

    def _get_search_configuration(self) -> tuple[list[str], list[str]]:
        table_details = self._fetch_table_details()
        ordered_column_names = table_details.ordered_column_names

        if not ordered_column_names:
            raise GoogleChronicleValidationError(
                f"Data table “{self.params.data_table_name}” has no columns "
                "defined with 'originalColumn' in 'columnInfo'."
            )

        self.soar_action.LOGGER.info(
            f"Data table schema columns (ordered): {', '.join(ordered_column_names)}."
        )

        columns_to_search = self.params.columns_to_search or ordered_column_names
        if self.params.columns_to_search:
            self._validate_specified_columns(columns_to_search, ordered_column_names)

        return ordered_column_names, columns_to_search

    def _process_value_searches(
        self, ordered_columns: list[str], columns_to_search: list[str]
    ) -> tuple[list[SingleJson], bool]:
        all_results = []
        found_any_match = False

        for value in self.params.values_to_search:
            self.soar_action.LOGGER.info(f"Searching for value: '{value}'")
            matched_rows = self._search_value_in_table(
                value_to_search=value,
                columns_to_search=columns_to_search,
                case_insensitive=self.params.case_insensitive_search,
                max_rows=self.params.max_data_table_rows_to_return,
                ordered_column_names=ordered_columns,
            )

            matched_rows_json = self._build_json_result(matched_rows, ordered_columns)
            all_results.append(
                {
                    "Entity": value,
                    "EntityResult": {
                        "is_found": bool(matched_rows),
                        "matched_rows": matched_rows_json,
                    },
                }
            )

            if matched_rows:
                found_any_match = True

        return all_results, found_any_match

    def _set_final_output(self, all_results: list[SingleJson], found_any: bool) -> None:
        self.json_results = all_results

        if found_any:
            self.output_message = (
                f"Successfully searched provided values in the data table "
                f"“{self.params.data_table_name}” in Google SecOps."
            )
        else:
            self.output_message = (
                f"No provided values were found in the data table "
                f"“{self.params.data_table_name}” in Google SecOps."
            )

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

        if table_details.name is None:
            raise GoogleChronicleValidationError(
                f"Data table “{self.params.data_table_name}” details response is "
                f"missing the 'name' (parent resource name). "
                f"API Response: {json.dumps(table_details.raw_data)}"
            )

        return table_details

    def _validate_specified_columns(
        self,
        specified_columns: list[str],
        available_columns: list[str],
    ) -> None:
        missing_columns = set(specified_columns) - set(available_columns)
        if missing_columns:
            missing_str = ", ".join(sorted(list(missing_columns)))
            raise GoogleChronicleManagerError(
                "The following columns were not found in the "
                f"{self.params.data_table_name}: {missing_str}. "
                "Please check the spelling."
            )
        self.soar_action.LOGGER.info(
            "Specified columns validated successfully against table schema."
        )

    def _search_value_in_table(
        self,
        value_to_search: str,
        columns_to_search: list[str],
        case_insensitive: bool,
        max_rows: int,
        ordered_column_names: list[str],
    ) -> list[AddedDataTableRow]:
        matched_rows: list[AddedDataTableRow] = []
        self.soar_action.LOGGER.info(
            f"Starting search for value '{value_to_search}' in table "
            f"'{self.params.data_table_name}' within columns: {columns_to_search}."
        )

        for row in self._paginated_list_rows(filter_query=value_to_search):
            if self._is_row_match(
                row,
                value_to_search,
                columns_to_search,
                case_insensitive,
                ordered_column_names,
            ):
                matched_rows.append(row)
                if len(matched_rows) >= max_rows:
                    break

        self.soar_action.LOGGER.info(
            f"Finished searching for value '{value_to_search}'. "
            f"Found {len(matched_rows)} matches."
        )
        return matched_rows

    def _paginated_list_rows(
        self,
        filter_query: str | None = None,
    ) -> Iterator[AddedDataTableRow]:
        self.soar_action.LOGGER.info(
            f"Fetching rows for table '{self.params.data_table_name}'..."
        )
        if filter_query:
            self.soar_action.LOGGER.info(f"Using server-side filter: '{filter_query}'")

        try:
            yield from self.api_client.list_all_data_table_rows(
                data_table_identifier=self.params.data_table_name,
                filter_query=filter_query,
            )
        except GoogleChronicleAPILimitError as e:
            raise GoogleChronicleAPILimitError(
                "reached an API rate limit for the action. Try again in 1 minute."
            ) from e

        except Exception as e:
            raise GoogleChronicleManagerError(
                f"Failed to list data table rows for table "
                f"“{self.params.data_table_name}”. API Error: {e}"
            ) from e

    def _is_row_match(
        self,
        row: AddedDataTableRow,
        value_to_search: str,
        columns_to_search: list[str],
        case_insensitive: bool,
        ordered_column_names: list[str],
    ) -> bool:
        row_values_dict = dict(zip(ordered_column_names, row.values))
        value_to_search_str = str(value_to_search)

        for col_name in columns_to_search:
            col_value = row_values_dict.get(col_name)
            if col_value is None:
                continue

            col_value_str = str(col_value).strip()

            search_term = (
                value_to_search_str.lower() if case_insensitive else value_to_search_str
            )
            value_in_row = col_value_str.lower() if case_insensitive else col_value_str

            if search_term == value_in_row:
                return True

        return False

    def _build_json_result(
        self, matched_rows: list[AddedDataTableRow], ordered_columns: list[str]
    ) -> list[SingleJson]:
        json_rows = []
        for row in matched_rows:
            row_json = row.to_json()
            row_json["values"] = dict(zip(ordered_columns, row.values))
            json_rows.append(row_json)
        return json_rows


def main() -> None:
    action = IsValueInDataTableAction()
    action.run()


if __name__ == "__main__":
    main()
