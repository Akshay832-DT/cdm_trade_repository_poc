"""
FIX MassCancelResponse field (tag 531).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MassCancelResponseValues:
    """Enumerated values for MassCancelResponse."""
    VALUE_0 = "0"  # CANCEL_REQUEST_REJECTED
    VALUE_1 = "1"  # CANCEL_ORDERS_FOR_A_SECURITY
    VALUE_2 = "2"  # CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY
    VALUE_3 = "3"  # CANCEL_ORDERS_FOR_A_PRODUCT
    VALUE_4 = "4"  # CANCEL_ORDERS_FOR_ACFI_CODE
    VALUE_5 = "5"  # CANCEL_ORDERS_FOR_A_SECURITY_TYPE
    VALUE_6 = "6"  # CANCEL_ORDERS_FOR_A_TRADING_SESSION
    VALUE_7 = "7"  # CANCEL_ALL_ORDERS

class MassCancelResponseField(FIXFieldBase):
    """"""
    tag: str = "531"
    name: str = "MassCancelResponse"
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
