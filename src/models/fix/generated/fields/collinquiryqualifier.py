"""
FIX CollInquiryQualifier field (tag 896).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CollInquiryQualifierValues:
    """Enumerated values for CollInquiryQualifier."""
    VALUE_0 = "0"  # TRADE_DATE
    VALUE_1 = "1"  # GC_INSTRUMENT
    VALUE_2 = "2"  # COLLATERAL_INSTRUMENT
    VALUE_3 = "3"  # SUBSTITUTION_ELIGIBLE
    VALUE_4 = "4"  # NOT_ASSIGNED
    VALUE_5 = "5"  # PARTIALLY_ASSIGNED
    VALUE_6 = "6"  # FULLY_ASSIGNED
    VALUE_7 = "7"  # OUTSTANDING_TRADES

class CollInquiryQualifierField(FIXFieldBase):
    """"""
    tag: str = "896"
    name: str = "CollInquiryQualifier"
    type: str = "INT"
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
