from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING

from TIPCommon.base.action import Action

from action_init import create_api_client
from XDRManager import XDRManager

if TYPE_CHECKING:
    import requests


class BaseAction(Action, ABC):
    """Base action class."""

    def _init_api_clients(self) -> XDRManager:
        """Prepare API client"""
        return create_api_client(self.soar_action)

    @property
    def result_value(self) -> bool:
        return self._result_value

    @result_value.setter
    def result_value(self, value: bool) -> None:
        self._result_value = value
