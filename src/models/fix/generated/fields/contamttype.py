"""
FIX ContAmtType field (tag 519).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ContAmtTypeValues:
    """Enumerated values for ContAmtType."""
    VALUE_1 = "1"  # COMMISSION_AMOUNT
    VALUE_2 = "2"  # COMMISSION_PERCENT
    VALUE_3 = "3"  # INITIAL_CHARGE_AMOUNT
    VALUE_4 = "4"  # INITIAL_CHARGE_PERCENT
    VALUE_5 = "5"  # DISCOUNT_AMOUNT
    VALUE_6 = "6"  # DISCOUNT_PERCENT
    VALUE_7 = "7"  # DILUTION_LEVY_AMOUNT
    VALUE_8 = "8"  # DILUTION_LEVY_PERCENT
    VALUE_9 = "9"  # EXIT_CHARGE_AMOUNT
    VALUE_10 = "10"  # EXIT_CHARGE_PERCENT
    VALUE_11 = "11"  # FUND_BASED_RENEWAL_COMMISSION_PERCENT
    VALUE_12 = "12"  # PROJECTED_FUND_VALUE
    VALUE_13 = "13"  # FUND_BASED_RENEWAL_COMMISSION_ON_ORDER
    VALUE_14 = "14"  # FUND_BASED_RENEWAL_COMMISSION_ON_FUND
    VALUE_15 = "15"  # NET_SETTLEMENT_AMOUNT

class ContAmtTypeField(FIXFieldBase):
    """"""
    tag: str = "519"
    name: str = "ContAmtType"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]

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
