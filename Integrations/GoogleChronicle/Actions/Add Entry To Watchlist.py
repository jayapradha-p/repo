from __future__ import annotations

from typing import TYPE_CHECKING

from TIPCommon.base.action import Action
from TIPCommon.extraction import extract_action_param, extract_configuration_param
from TIPCommon import validation
from TIPCommon.utils import is_empty_string_or_none

import consts
from exceptions import InvalidParameterError
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2
from utils import validate_api_root_for_backstory

if TYPE_CHECKING:
    from typing import Never

    from TIPCommon.types import SingleJson

    from datamodels import Watchlist, WatchlistEntity


class AddEntryToWatchlist(Action):
    """SOAR action to add an entity entry to a Chronicle Watchlist."""

    def __init__(self) -> None:
        super().__init__(consts.ADD_ENTRY_TO_WATCHLIST_SCRIPT_NAME)

    def _extract_action_parameters(self) -> None:
        """Extract action and configuration parameters."""
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

        self.params.watchlist_name = extract_action_param(
            self.soar_action,
            param_name="Watchlist Name",
            is_mandatory=True,
            print_value=True,
        )
        self.params.entry = extract_action_param(
            self.soar_action,
            param_name="Entry",
            is_mandatory=True,
            print_value=True,
        )

    def _validate_params(self) -> None:
        """Validate configuration and action parameters."""
        validator: validation.ParameterValidator = validation.ParameterValidator(
            self.soar_action
        )

        if not is_empty_string_or_none(self.params.user_service_account):
            self.params.user_service_account = validator.validate_json(
                param_name="User's Service Account",
                json_string=self.params.user_service_account,
                print_value=False,
            )

        validate_api_root_for_backstory(self.params.api_root)

        self.params.entry = validator.validate_json(
            param_name="Entry",
            json_string=self.params.entry,
        )

    def _init_api_clients(self) -> GoogleChronicleManagerV2:
        """Initialize Chronicle manager."""
        return GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=self.params.user_service_account,
            chronicle_soar=self.soar_action,
            api_root=self.params.api_root,
            verify_ssl=self.params.verify_ssl,
            workload_identity_email=self.params.workload_identity_email,
        )

    def _perform_action(self, _: Never) -> None:
        watchlist: Watchlist | None = self.api_client.get_watchlist_by_name(
            self.params.watchlist_name
        )
        if watchlist is None:
            raise InvalidParameterError(
                f"Watchlist '{self.params.watchlist_name}' not found."
            )

        formatted_entries: list[SingleJson] = self._normalize_and_format_entries()
        results: list[WatchlistEntity] = self.api_client.add_entry_to_watchlist(
            watchlist.watchlist_id,
            formatted_entries,
        )
        self.output_message = (
            "Successfully added new entries to a watchlist "
            f'"{self.params.watchlist_name}" in Google SecOps.'
        )
        self.json_results = [entry.to_json() for entry in results]

    def _normalize_and_format_entries(self) -> list[SingleJson]:
        """Normalize entries into a list and format each one."""
        raw_entries = (
            self.params.entry
            if isinstance(self.params.entry, list)
            else [self.params.entry]
        )
        return [_format_single_entity(entry) for entry in raw_entries]


def _format_single_entity(entry: SingleJson) -> SingleJson:
    """Convert a single entry dict into Chronicle API format.
    1. Validate the entry structure.
    2. Format the entry according to its type.
    Args:
        entry (SingleJson): The raw entry dictionary.

    Returns:
        SingleJson: The formatted entry dictionary.

    Raises:
        InvalidParameterError: If the entry is invalid.
    """
    _validate_single_entry(entry)

    entity_type: str = entry["type"]
    entity_value: str = entry["entity"]
    namespace: str | None = entry.get("namespace")

    formatter: callable = consts.ENTITY_TYPE_MAPPING[entity_type]
    formatted_body: SingleJson = formatter(entity_value)

    inner_entity: SingleJson = {**formatted_body}
    if namespace is not None:
        inner_entity["namespace"] = namespace

    return {"entity": {"entity": inner_entity}}


def _validate_single_entry(entry: SingleJson) -> None:
    """Validate the structure of a single entry.

    Args:
        entry (SingleJson): The raw entry dictionary.

    Raises:
        InvalidParameterError: If the entry is invalid.
    """
    entity_value: str | None = entry.get("entity")
    entity_type: str = entry.get("type")

    if not entity_value:
        raise InvalidParameterError("Each entry must contain an 'entity' field.")

    if entity_type not in consts.ENTITY_TYPE_MAPPING:
        allowed: str = ", ".join(sorted(consts.ENTITY_TYPE_MAPPING.keys()))
        raise InvalidParameterError(
            f"Invalid entity type '{entity_type}'. Expected one of: {allowed}"
        )


def main() -> None:
    action = AddEntryToWatchlist()
    action.run()


if __name__ == "__main__":
    main()
