"""
FIX MassStatusReqType field (tag 585).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MassStatusReqTypeValues:
    """Enumerated values for MassStatusReqType."""
    VALUE_1 = "1"  # STATUS_FOR_ORDERS_FOR_A_SECURITY
    VALUE_2 = "2"  # STATUS_FOR_ORDERS_FOR_AN_UNDERLYING_SECURITY
    VALUE_3 = "3"  # STATUS_FOR_ORDERS_FOR_A_PRODUCT
    VALUE_4 = "4"  # STATUS_FOR_ORDERS_FOR_ACFI_CODE
    VALUE_5 = "5"  # STATUS_FOR_ORDERS_FOR_A_SECURITY_TYPE
    VALUE_6 = "6"  # STATUS_FOR_ORDERS_FOR_A_TRADING_SESSION
    VALUE_7 = "7"  # STATUS_FOR_ALL_ORDERS
    VALUE_8 = "8"  # STATUS_FOR_ORDERS_FOR_A_PARTY_ID

class MassStatusReqTypeField(FIXFieldBase):
    """"""
    tag: str = "585"
    name: str = "MassStatusReqType"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8"]

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
