"""
FIX RegistRejReasonCode field (tag 507).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RegistRejReasonCodeValues:
    """Enumerated values for RegistRejReasonCode."""
    VALUE_1 = "1"  # INVALID_ACCOUNT_TYPE
    VALUE_2 = "2"  # INVALID_TAX_EXEMPT_TYPE
    VALUE_3 = "3"  # INVALID_OWNERSHIP_TYPE
    VALUE_4 = "4"  # NO_REG_DETAILS
    VALUE_5 = "5"  # INVALID_REG_SEQ_NO
    VALUE_6 = "6"  # INVALID_REG_DETAILS
    VALUE_7 = "7"  # INVALID_MAILING_DETAILS
    VALUE_8 = "8"  # INVALID_MAILING_INSTRUCTIONS
    VALUE_9 = "9"  # INVALID_INVESTOR_ID
    VALUE_10 = "10"  # INVALID_INVESTOR_ID_SOURCE
    VALUE_11 = "11"  # INVALID_DATE_OF_BIRTH
    VALUE_12 = "12"  # INVALID_COUNTRY
    VALUE_13 = "13"  # INVALID_DISTRIB_INSTNS
    VALUE_14 = "14"  # INVALID_PERCENTAGE
    VALUE_15 = "15"  # INVALID_PAYMENT_METHOD
    VALUE_16 = "16"  # INVALID_ACCOUNT_NAME
    VALUE_17 = "17"  # INVALID_AGENT_CODE
    VALUE_18 = "18"  # INVALID_ACCOUNT_NUM
    VALUE_99 = "99"  # OTHER

class RegistRejReasonCodeField(FIXFieldBase):
    """"""
    tag: str = "507"
    name: str = "RegistRejReasonCode"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "99"]

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
    @property
    def is_value_13(self) -> bool:
        return self.value == "13"
    @property
    def is_value_14(self) -> bool:
        return self.value == "14"
    @property
    def is_value_15(self) -> bool:
        return self.value == "15"
    @property
    def is_value_16(self) -> bool:
        return self.value == "16"
    @property
    def is_value_17(self) -> bool:
        return self.value == "17"
    @property
    def is_value_18(self) -> bool:
        return self.value == "18"
    @property
    def is_value_99(self) -> bool:
        return self.value == "99"
