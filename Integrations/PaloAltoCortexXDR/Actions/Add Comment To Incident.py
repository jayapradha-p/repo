from __future__ import annotations

from typing import TYPE_CHECKING

from TIPCommon.extraction import extract_action_param

import action_init
from base_action import BaseAction
from constants import (
    ADD_COMMENT_TO_INCIDENT_ACTION_SCRIPT_NAME,
    ID_NOT_FOUND,
    INTEGRATION_NAME,
)
import exceptions

if TYPE_CHECKING:
    from typing import NoReturn

    from XDRManager import XDRManager


class AddCommentToIncidentAction(BaseAction):
    def __init__(self) -> None:
        super().__init__(ADD_COMMENT_TO_INCIDENT_ACTION_SCRIPT_NAME)

    def _extract_action_parameters(self) -> None:
        self.params.incident_id = extract_action_param(
            self.soar_action,
            param_name="Incident ID",
            is_mandatory=True,
            print_value=True,
        )
        self.params.comment: str = extract_action_param(
            self.soar_action,
            param_name="Comment",
            is_mandatory=True,
        )

    def _init_api_clients(self) -> XDRManager:
        return action_init.create_api_client(self.soar_action)

    def _perform_action(self, _) -> None:
        try:
            self.api_client.add_comment_to_incident(
                incident_id=self.params.incident_id,
                comment=self.params.comment,
            )
            self.output_message = (
                "Successfully add a comment to an incident with ID "
                f"{self.params.incident_id} in {INTEGRATION_NAME}."
            )
        except exceptions.XDRException as e:
            if ID_NOT_FOUND in str(e).lower():
                raise exceptions.XDRNotFoundException(
                    f"Incident with ID {self.params.incident_id} was not found."
                ) from e
            raise


def main() -> NoReturn:
    AddCommentToIncidentAction().run()


if __name__ == "__main__":
    main()
