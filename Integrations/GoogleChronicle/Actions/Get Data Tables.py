from __future__ import annotations

from typing import Any

from TIPCommon.base.action import Action
from TIPCommon.extraction import extract_action_param, extract_configuration_param
from TIPCommon import validation
from TIPCommon.utils import is_empty_string_or_none
from TIPCommon.types import SingleJson

import consts
import datamodels
import exceptions
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2
from utils import validate_api_root_for_backstory


class GetDataTables(Action):

    def __init__(self) -> None:
        super().__init__(consts.GET_DATA_TABLES_SCRIPT_NAME)
        self.error_output_message: str = "Error executing action " f'"{self.name}".'
        self.output_message: str = ""
        self.result_value: bool = False
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
        self.params.filter_key = extract_action_param(
            self.soar_action,
            param_name="Filter Key",
            print_value=True,
        )
        self.params.filter_logic = extract_action_param(
            self.soar_action,
            param_name="Filter Logic",
            print_value=True,
        )
        self.params.filter_value = extract_action_param(
            self.soar_action,
            param_name="Filter Value",
            print_value=True,
        )
        self.params.expanded_rows = extract_action_param(
            self.soar_action,
            param_name="Expanded Rows",
            input_type=bool,
            default_value=False,
            print_value=True,
        )
        self.params.max_data_tables_to_return = extract_action_param(
            self.soar_action,
            param_name="Max Data Tables To Return",
            input_type=int,
            print_value=True,
            default_value=consts.DEFAULT_MAX_DATA_TABLES_TO_RETURN,
        )
        self.params.max_data_table_rows_to_return = extract_action_param(
            self.soar_action,
            param_name="Max Data Table Rows To Return",
            input_type=int,
            print_value=True,
            default_value=consts.DEFAULT_MAX_DATA_TABLE_ROWS_TO_RETURN,
        )

    def _validate_params(self) -> None:
        validate_api_root_for_backstory(self.params.api_root)
        validator = validation.ParameterValidator(self.soar_action)
        if not is_empty_string_or_none(self.params.user_service_account):
            self.params.user_service_account = validator.validate_json(
                param_name="User's Service Account",
                json_string=self.params.user_service_account,
                print_value=False,
            )
        self.params.filter_key = validator.validate_ddl(
            param_name="Filter Key",
            value=self.params.filter_key,
            ddl_values=consts.GET_DATA_TABLES_FILTER_KEY_DDL_VALUES,
            default_value=consts.GET_DATA_TABLES_FILTER_KEY_DEFAULT_VALUE,
        )
        self.params.filter_logic = validator.validate_ddl(
            param_name="Filter Logic",
            value=self.params.filter_logic,
            ddl_values=consts.GET_DATA_TABLES_FILTER_LOGIC_DDL_VALUES,
            default_value=consts.GET_DATA_TABLES_FILTER_LOGIC_EQUAL,
        )

        if (
            self.params.filter_key == consts.GET_DATA_TABLES_FILTER_KEY_DEFAULT_VALUE
            and self.params.filter_logic
            in (
                consts.GET_DATA_TABLES_FILTER_LOGIC_EQUAL,
                consts.GET_DATA_TABLES_FILTER_LOGIC_CONTAINS,
            )
        ):
            raise exceptions.GoogleChronicleManagerError(
                'you need to select a field from the "Filter Key" parameter.'
            )

        validator.validate_range(
            param_name="Max Data Tables To Return",
            value=self.params.max_data_tables_to_return,
            min_limit=consts.MIN_DATA_TABLES,
            max_limit=consts.MAX_DATA_TABLES,
        )
        validator.validate_range(
            param_name="Max Data Table Rows To Return",
            value=self.params.max_data_table_rows_to_return,
            min_limit=consts.MIN_DATA_TABLE_ROWS,
            max_limit=consts.MAX_DATA_TABLE_ROWS,
        )

    def _init_api_clients(self) -> GoogleChronicleManagerV2:
        return GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=self.params.user_service_account,
            chronicle_soar=self.soar_action,
            api_root=self.params.api_root,
            verify_ssl=self.params.verify_ssl,
            workload_identity_email=self.params.workload_identity_email,
        )

    def _perform_action(self, _: Any = None) -> None:
        fetched_data_tables = self._fetch_data_tables()
        self._process_fetched_data_tables(fetched_data_tables)

    def _fetch_data_tables(self) -> list[datamodels.DataTableDetails]:
        return self._fetch_data_table_by_key(self.params.filter_key)

    def _fetch_data_table_by_key(self, key: str) -> list[datamodels.DataTableDetails]:
        exact_match = (
            self.params.filter_logic == consts.GET_DATA_TABLES_FILTER_LOGIC_EQUAL
        )
        filter_value = self.params.filter_value

        if (
            key == consts.GET_DATA_TABLES_FILTER_KEY_NAME
            and exact_match
            and filter_value
        ):
            table = self.api_client.data_table_details(
                data_table_identifier=filter_value,
                action_name="GetDataTables",
                expanded_rows=self.params.expanded_rows,
                max_data_table_rows=self.params.max_data_table_rows_to_return,
            )
            return [table] if table else []

        tables = self._fetch_multiple_data_tables()

        if filter_value:
            tables = self._apply_filter(
                tables,
                key,
                self.params.filter_logic,
                filter_value,
            )[: self.params.max_data_tables_to_return]

        if self.params.expanded_rows:
            tables = [
                self.api_client.enrich_data_table_with_rows(
                    table,
                    self.params.max_data_table_rows_to_return,
                )
                for table in tables
            ]

        return tables

    def _fetch_multiple_data_tables(self) -> list[datamodels.DataTableDetails]:
        return self.api_client.get_all_data_tables()

    def _apply_filter(
        self,
        tables: list[datamodels.DataTableDetails],
        key: str,
        logic: str,
        value: str,
    ) -> list[datamodels.DataTableDetails]:
        def matches(table: datamodels.DataTableDetails) -> bool:
            attr = getattr(
                table,
                (
                    "display_name"
                    if key == consts.GET_DATA_TABLES_FILTER_KEY_NAME
                    else "description"
                ),
                None,
            )
            if not attr:
                return False

            if logic == consts.GET_DATA_TABLES_FILTER_LOGIC_EQUAL:
                return attr == value

            if logic == consts.GET_DATA_TABLES_FILTER_LOGIC_CONTAINS:
                return value.lower() in attr.lower()

            return False

        return [table for table in tables if matches(table)]

    def _process_fetched_data_tables(
        self,
        data_tables: list[datamodels.DataTableDetails],
    ) -> None:
        if not data_tables:
            self._handle_no_data_tables_found()
        else:
            self.result_value = True
            self.output_message = (
                "Successfully found data tables for the provided criteria "
                "in Google SecOps."
            )
            self._add_data_tables_to_results(data_tables)

    def _add_data_tables_to_results(
        self,
        data_tables: list[datamodels.DataTableDetails],
    ) -> None:
        json_results = [dt.to_json() for dt in data_tables]
        self.soar_action.result.add_result_json(json_results)

    def _handle_no_data_tables_found(self) -> None:
        self.output_message = (
            "No data tables were found for the provided criteria in Google SecOps."
        )
        self.result_value = False


def main() -> None:
    GetDataTables().run()


if __name__ == "__main__":
    main()
