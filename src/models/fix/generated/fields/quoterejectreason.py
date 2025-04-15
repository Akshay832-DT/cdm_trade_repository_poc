"""
FIX QuoteRejectReason field (tag 300).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteRejectReasonValues:
    """Enumerated values for QuoteRejectReason."""
    VALUE_1 = "1"  # UNKNOWN_SYMBOL
    VALUE_2 = "2"  # EXCHANGE
    VALUE_3 = "3"  # QUOTE_REQUEST_EXCEEDS_LIMIT
    VALUE_4 = "4"  # TOO_LATE_TO_ENTER
    VALUE_5 = "5"  # UNKNOWN_QUOTE
    VALUE_6 = "6"  # DUPLICATE_QUOTE
    VALUE_7 = "7"  # INVALID_BID
    VALUE_8 = "8"  # INVALID_PRICE
    VALUE_9 = "9"  # NOT_AUTHORIZED_TO_QUOTE_SECURITY
    VALUE_99 = "99"  # OTHER

class QuoteRejectReasonField(FIXFieldBase):
    """"""
    tag: str = "300"
    name: str = "QuoteRejectReason"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "99"]

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
    def is_value_99(self) -> bool:
        return self.value == "99"
