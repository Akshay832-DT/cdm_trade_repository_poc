"""
FIX QuoteStatus field (tag 297).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteStatusValues:
    """Enumerated values for QuoteStatus."""
    VALUE_0 = "0"  # ACCEPTED
    VALUE_1 = "1"  # CANCEL_FOR_SYMBOL
    VALUE_2 = "2"  # CANCELED_FOR_SECURITY_TYPE
    VALUE_3 = "3"  # CANCELED_FOR_UNDERLYING
    VALUE_4 = "4"  # CANCELED_ALL
    VALUE_5 = "5"  # REJECTED
    VALUE_6 = "6"  # REMOVED_FROM_MARKET
    VALUE_7 = "7"  # EXPIRED
    VALUE_8 = "8"  # QUERY
    VALUE_9 = "9"  # QUOTE_NOT_FOUND
    VALUE_10 = "10"  # PENDING
    VALUE_11 = "11"  # PASS
    VALUE_12 = "12"  # LOCKED_MARKET_WARNING
    VALUE_13 = "13"  # CROSS_MARKET_WARNING
    VALUE_14 = "14"  # CANCELED_DUE_TO_LOCK_MARKET
    VALUE_15 = "15"  # CANCELED_DUE_TO_CROSS_MARKET

class QuoteStatusField(FIXFieldBase):
    """"""
    tag: str = "297"
    name: str = "QuoteStatus"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]

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
