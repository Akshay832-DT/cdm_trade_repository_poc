"""
FIX AllocRejCode field (tag 88).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocRejCodeValues:
    """Enumerated values for AllocRejCode."""
    VALUE_0 = "0"  # UNKNOWN_ACCOUNT
    VALUE_1 = "1"  # INCORRECT_QUANTITY
    VALUE_2 = "2"  # INCORRECT_AVERAGEG_PRICE
    VALUE_3 = "3"  # UNKNOWN_EXECUTING_BROKER_MNEMONIC
    VALUE_4 = "4"  # COMMISSION_DIFFERENCE
    VALUE_5 = "5"  # UNKNOWN_ORDER_ID
    VALUE_6 = "6"  # UNKNOWN_LIST_ID
    VALUE_7 = "7"  # OTHER_SEE_TEXT
    VALUE_8 = "8"  # INCORRECT_ALLOCATED_QUANTITY
    VALUE_9 = "9"  # CALCULATION_DIFFERENCE
    VALUE_10 = "10"  # UNKNOWN_OR_STALE_EXEC_ID
    VALUE_11 = "11"  # MISMATCHED_DATA
    VALUE_12 = "12"  # UNKNOWN_CL_ORD_ID
    VALUE_13 = "13"  # WAREHOUSE_REQUEST_REJECTED

class AllocRejCodeField(FIXFieldBase):
    """"""
    tag: str = "88"
    name: str = "AllocRejCode"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

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
    @property
    def is_value_10(self) -> bool:
        return self.value == "10"
    @property
    def is_value_11(self) -> bool:
        return self.value == "11"
    @property
    def is_value_12(self) -> bool:
        return self.value == "12"
    @property
    def is_value_13(self) -> bool:
        return self.value == "13"
