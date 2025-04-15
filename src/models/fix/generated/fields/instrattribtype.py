"""
FIX InstrAttribType field (tag 871).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class InstrAttribTypeValues:
    """Enumerated values for InstrAttribType."""
    VALUE_1 = "1"  # FLAT
    VALUE_2 = "2"  # ZERO_COUPON
    VALUE_3 = "3"  # INTEREST_BEARING
    VALUE_4 = "4"  # NO_PERIODIC_PAYMENTS
    VALUE_5 = "5"  # VARIABLE_RATE
    VALUE_6 = "6"  # LESS_FEE_FOR_PUT
    VALUE_7 = "7"  # STEPPED_COUPON
    VALUE_8 = "8"  # COUPON_PERIOD
    VALUE_9 = "9"  # WHEN
    VALUE_10 = "10"  # ORIGINAL_ISSUE_DISCOUNT
    VALUE_11 = "11"  # CALLABLE
    VALUE_12 = "12"  # ESCROWED_TO_MATURITY
    VALUE_13 = "13"  # ESCROWED_TO_REDEMPTION_DATE
    VALUE_14 = "14"  # PRE_REFUNDED
    VALUE_15 = "15"  # IN_DEFAULT
    VALUE_16 = "16"  # UNRATED
    VALUE_17 = "17"  # TAXABLE
    VALUE_18 = "18"  # INDEXED
    VALUE_19 = "19"  # SUBJECT_TO_ALTERNATIVE_MINIMUM_TAX
    VALUE_20 = "20"  # ORIGINAL_ISSUE_DISCOUNT_PRICE
    VALUE_21 = "21"  # CALLABLE_BELOW_MATURITY_VALUE
    VALUE_22 = "22"  # CALLABLE_WITHOUT_NOTICE
    VALUE_99 = "99"  # TEXT

class InstrAttribTypeField(FIXFieldBase):
    """"""
    tag: str = "871"
    name: str = "InstrAttribType"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "99"]

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
    def is_value_19(self) -> bool:
        return self.value == "19"
    @property
    def is_value_20(self) -> bool:
        return self.value == "20"
    @property
    def is_value_21(self) -> bool:
        return self.value == "21"
    @property
    def is_value_22(self) -> bool:
        return self.value == "22"
    @property
    def is_value_99(self) -> bool:
        return self.value == "99"
