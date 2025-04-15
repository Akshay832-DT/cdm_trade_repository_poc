"""
FIX QuoteRequestRejectReason field (tag 658).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteRequestRejectReasonValues:
    """Enumerated values for QuoteRequestRejectReason."""
    VALUE_1 = "1"  # UNKNOWN_SYMBOL
    VALUE_2 = "2"  # EXCHANGE
    VALUE_3 = "3"  # QUOTE_REQUEST_EXCEEDS_LIMIT
    VALUE_4 = "4"  # TOO_LATE_TO_ENTER
    VALUE_5 = "5"  # INVALID_PRICE
    VALUE_6 = "6"  # NOT_AUTHORIZED_TO_REQUEST_QUOTE
    VALUE_7 = "7"  # NO_MATCH_FOR_INQUIRY
    VALUE_8 = "8"  # NO_MARKET_FOR_INSTRUMENT
    VALUE_9 = "9"  # NO_INVENTORY
    VALUE_10 = "10"  # PASS
    VALUE_99 = "99"  # OTHER

class QuoteRequestRejectReasonField(FIXFieldBase):
    """"""
    tag: str = "658"
    name: str = "QuoteRequestRejectReason"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "99"]

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
    def is_value_99(self) -> bool:
        return self.value == "99"
