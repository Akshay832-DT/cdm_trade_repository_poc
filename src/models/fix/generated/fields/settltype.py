"""
FIX SettlType field (tag 63).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlTypeValues:
    """Enumerated values for SettlType."""
    VALUE_0 = "0"  # REGULAR
    VALUE_1 = "1"  # CASH
    VALUE_2 = "2"  # NEXT_DAY
    VALUE_3 = "3"  # T_PLUS2
    VALUE_4 = "4"  # T_PLUS3
    VALUE_5 = "5"  # T_PLUS4
    VALUE_6 = "6"  # FUTURE
    VALUE_7 = "7"  # WHEN_AND_IF_ISSUED
    VALUE_8 = "8"  # SELLERS_OPTION
    VALUE_9 = "9"  # T_PLUS5

class SettlTypeField(FIXFieldBase):
    """"""
    tag: str = "63"
    name: str = "SettlType"
    type: str = "CHAR"
    value: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

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
    @property
    def is_value_8(self) -> bool:
        return self.value == "8"
    @property
    def is_value_9(self) -> bool:
        return self.value == "9"
