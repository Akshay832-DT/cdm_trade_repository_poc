"""
FIX OwnerType field (tag 522).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OwnerTypeValues:
    """Enumerated values for OwnerType."""
    VALUE_1 = "1"  # INDIVIDUAL_INVESTOR
    VALUE_2 = "2"  # PUBLIC_COMPANY
    VALUE_3 = "3"  # PRIVATE_COMPANY
    VALUE_4 = "4"  # INDIVIDUAL_TRUSTEE
    VALUE_5 = "5"  # COMPANY_TRUSTEE
    VALUE_6 = "6"  # PENSION_PLAN
    VALUE_7 = "7"  # CUSTODIAN_UNDER_GIFTS_TO_MINORS_ACT
    VALUE_8 = "8"  # TRUSTS
    VALUE_9 = "9"  # FIDUCIARIES
    VALUE_10 = "10"  # NETWORKING_SUB_ACCOUNT
    VALUE_11 = "11"  # NON_PROFIT_ORGANIZATION
    VALUE_12 = "12"  # CORPORATE_BODY
    VALUE_13 = "13"  # NOMINEE

class OwnerTypeField(FIXFieldBase):
    """"""
    tag: str = "522"
    name: str = "OwnerType"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

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
