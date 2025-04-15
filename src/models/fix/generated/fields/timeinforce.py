"""
FIX TimeInForce field (tag 59).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TimeInForceValues:
    """Enumerated values for TimeInForce."""
    VALUE_0 = "0"  # DAY
    VALUE_1 = "1"  # GOOD_TILL_CANCEL
    VALUE_2 = "2"  # AT_THE_OPENING
    VALUE_3 = "3"  # IMMEDIATE_OR_CANCEL
    VALUE_4 = "4"  # FILL_OR_KILL
    VALUE_5 = "5"  # GOOD_TILL_CROSSING
    VALUE_6 = "6"  # GOOD_TILL_DATE
    VALUE_7 = "7"  # AT_THE_CLOSE

class TimeInForceField(FIXFieldBase):
    """"""
    tag: str = "59"
    name: str = "TimeInForce"
    type: str = "CHAR"
    value: Literal["0", "1", "2", "3", "4", "5", "6", "7"]

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
    def is_value_3(self) -> bool:
        return self.value == "3"
    @property
    def is_value_4(self) -> bool:
        return self.value == "4"
    @property
    def is_value_5(self) -> bool:
        return self.value == "5"
    @property
    def is_value_6(self) -> bool:
        return self.value == "6"
    @property
    def is_value_7(self) -> bool:
        return self.value == "7"
