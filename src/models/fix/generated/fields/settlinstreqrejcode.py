"""
FIX SettlInstReqRejCode field (tag 792).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlInstReqRejCodeValues:
    """Enumerated values for SettlInstReqRejCode."""
    VALUE_0 = "0"  # UNABLE_TO_PROCESS_REQUEST
    VALUE_1 = "1"  # UNKNOWN_ACCOUNT
    VALUE_2 = "2"  # NO_MATCHING_SETTLEMENT_INSTRUCTIONS_FOUND
    VALUE_99 = "99"  # OTHER

class SettlInstReqRejCodeField(FIXFieldBase):
    """"""
    tag: str = "792"
    name: str = "SettlInstReqRejCode"
    type: str = "INT"
    value: Literal["0", "1", "2", "99"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
    @property
    def is_value_99(self) -> bool:
        return self.value == "99"
