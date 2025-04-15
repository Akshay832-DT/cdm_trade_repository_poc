"""
FIX MiscFeeType field (tag 139).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MiscFeeTypeValues:
    """Enumerated values for MiscFeeType."""
    VALUE_1 = "1"  # REGULATORY
    VALUE_2 = "2"  # TAX
    VALUE_3 = "3"  # LOCAL_COMMISSION
    VALUE_4 = "4"  # EXCHANGE_FEES
    VALUE_5 = "5"  # STAMP
    VALUE_6 = "6"  # LEVY
    VALUE_7 = "7"  # OTHER
    VALUE_8 = "8"  # MARKUP
    VALUE_9 = "9"  # CONSUMPTION_TAX
    VALUE_10 = "10"  # PER_TRANSACTION
    VALUE_11 = "11"  # CONVERSION
    VALUE_12 = "12"  # AGENT

class MiscFeeTypeField(FIXFieldBase):
    """"""
    tag: str = "139"
    name: str = "MiscFeeType"
    type: str = "CHAR"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

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
