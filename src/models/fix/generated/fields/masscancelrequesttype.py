"""
FIX MassCancelRequestType field (tag 530).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MassCancelRequestTypeValues:
    """Enumerated values for MassCancelRequestType."""
    VALUE_1 = "1"  # CANCEL_ORDERS_FOR_A_SECURITY
    VALUE_2 = "2"  # CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY
    VALUE_3 = "3"  # CANCEL_ORDERS_FOR_A_PRODUCT
    VALUE_4 = "4"  # CANCEL_ORDERS_FOR_ACFI_CODE
    VALUE_5 = "5"  # CANCEL_ORDERS_FOR_A_SECURITY_TYPE
    VALUE_6 = "6"  # CANCEL_ORDERS_FOR_A_TRADING_SESSION
    VALUE_7 = "7"  # CANCEL_ALL_ORDERS

class MassCancelRequestTypeField(FIXFieldBase):
    """"""
    tag: str = "530"
    name: str = "MassCancelRequestType"
    type: str = "CHAR"
    value: Literal["1", "2", "3", "4", "5", "6", "7"]

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
