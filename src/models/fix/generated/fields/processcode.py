"""
FIX ProcessCode field (tag 81).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ProcessCodeValues:
    """Enumerated values for ProcessCode."""
    VALUE_0 = "0"  # REGULAR
    VALUE_1 = "1"  # SOFT_DOLLAR
    VALUE_2 = "2"  # STEP_IN
    VALUE_3 = "3"  # STEP_OUT
    VALUE_4 = "4"  # SOFT_DOLLAR_STEP_IN
    VALUE_5 = "5"  # SOFT_DOLLAR_STEP_OUT
    VALUE_6 = "6"  # PLAN_SPONSOR

class ProcessCodeField(FIXFieldBase):
    """"""
    tag: str = "81"
    name: str = "ProcessCode"
    type: str = "CHAR"
    value: Literal["0", "1", "2", "3", "4", "5", "6"]

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
