"""
FIX QuotePriceType field (tag 692).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuotePriceTypeValues:
    """Enumerated values for QuotePriceType."""
    VALUE_1 = "1"  # PERCENT
    VALUE_2 = "2"  # PER_SHARE
    VALUE_3 = "3"  # FIXED_AMOUNT
    VALUE_4 = "4"  # DISCOUNT
    VALUE_5 = "5"  # PREMIUM
    VALUE_6 = "6"  # SPREAD
    VALUE_7 = "7"  # TED_PRICE
    VALUE_8 = "8"  # TED_YIELD
    VALUE_9 = "9"  # YIELD_SPREAD
    VALUE_10 = "10"  # YIELD

class QuotePriceTypeField(FIXFieldBase):
    """"""
    tag: str = "692"
    name: str = "QuotePriceType"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

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
