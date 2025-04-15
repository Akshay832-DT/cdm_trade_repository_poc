"""
FIX ConfirmStatus field (tag 665).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ConfirmStatusValues:
    """Enumerated values for ConfirmStatus."""
    VALUE_1 = "1"  # RECEIVED
    VALUE_2 = "2"  # MISMATCHED_ACCOUNT
    VALUE_3 = "3"  # MISSING_SETTLEMENT_INSTRUCTIONS
    VALUE_4 = "4"  # CONFIRMED
    VALUE_5 = "5"  # REQUEST_REJECTED

class ConfirmStatusField(FIXFieldBase):
    """"""
    tag: str = "665"
    name: str = "ConfirmStatus"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
    @property
    def is_value_3(self) -> bool:
        return self.value == "3"
    @property
    def is_value_4(self) -> bool:
        return self.value == "4"
    @property
    def is_value_5(self) -> bool:
        return self.value == "5"
