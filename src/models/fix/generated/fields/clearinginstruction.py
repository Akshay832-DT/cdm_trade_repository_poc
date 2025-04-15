"""
FIX ClearingInstruction field (tag 577).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ClearingInstructionValues:
    """Enumerated values for ClearingInstruction."""
    VALUE_0 = "0"  # PROCESS_NORMALLY
    VALUE_1 = "1"  # EXCLUDE_FROM_ALL_NETTING
    VALUE_2 = "2"  # BILATERAL_NETTING_ONLY
    VALUE_3 = "3"  # EX_CLEARING
    VALUE_4 = "4"  # SPECIAL_TRADE
    VALUE_5 = "5"  # MULTILATERAL_NETTING
    VALUE_6 = "6"  # CLEAR_AGAINST_CENTRAL_COUNTERPARTY
    VALUE_7 = "7"  # EXCLUDE_FROM_CENTRAL_COUNTERPARTY
    VALUE_8 = "8"  # MANUAL_MODE
    VALUE_9 = "9"  # AUTOMATIC_POSTING_MODE
    VALUE_10 = "10"  # AUTOMATIC_GIVE_UP_MODE
    VALUE_11 = "11"  # QUALIFIED_SERVICE_REPRESENTATIVE_QSR
    VALUE_12 = "12"  # CUSTOMER_TRADE
    VALUE_13 = "13"  # SELF_CLEARING

class ClearingInstructionField(FIXFieldBase):
    """"""
    tag: str = "577"
    name: str = "ClearingInstruction"
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
