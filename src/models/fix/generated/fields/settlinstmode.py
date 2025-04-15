"""
FIX SettlInstMode field (tag 160).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlInstModeValues:
    """Enumerated values for SettlInstMode."""
    VALUE_1 = "1"  # STANDING_INSTRUCTIONS_PROVIDED
    VALUE_4 = "4"  # SPECIFIC_ORDER_FOR_A_SINGLE_ACCOUNT
    VALUE_5 = "5"  # REQUEST_REJECT

class SettlInstModeField(FIXFieldBase):
    """"""
    tag: str = "160"
    name: str = "SettlInstMode"
    type: str = "CHAR"
    value: Literal["1", "4", "5"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_4(self) -> bool:
        return self.value == "4"
    @property
    def is_value_5(self) -> bool:
        return self.value == "5"
