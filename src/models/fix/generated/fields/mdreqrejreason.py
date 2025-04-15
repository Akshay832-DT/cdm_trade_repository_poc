"""
FIX MDReqRejReason field (tag 281).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDReqRejReasonValues:
    """Enumerated values for MDReqRejReason."""
    VALUE_0 = "0"  # UNKNOWN_SYMBOL
    VALUE_1 = "1"  # DUPLICATE_MD_REQ_ID
    VALUE_2 = "2"  # INSUFFICIENT_BANDWIDTH
    VALUE_3 = "3"  # INSUFFICIENT_PERMISSIONS
    VALUE_4 = "4"  # UNSUPPORTED_SUBSCRIPTION_REQUEST_TYPE
    VALUE_5 = "5"  # UNSUPPORTED_MARKET_DEPTH
    VALUE_6 = "6"  # UNSUPPORTED_MD_UPDATE_TYPE
    VALUE_7 = "7"  # UNSUPPORTED_AGGREGATED_BOOK
    VALUE_8 = "8"  # UNSUPPORTED_MD_ENTRY_TYPE
    VALUE_9 = "9"  # UNSUPPORTED_TRADING_SESSION_ID
    A = "A"  # UNSUPPORTED_SCOPE
    B = "B"  # UNSUPPORTED_OPEN_CLOSE_SETTLE_FLAG
    C = "C"  # UNSUPPORTED_MD_IMPLICIT_DELETE

class MDReqRejReasonField(FIXFieldBase):
    """"""
    tag: str = "281"
    name: str = "MDReqRejReason"
    type: str = "CHAR"
    value: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C"]

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
    def is_a(self) -> bool:
        return self.value == "A"
    @property
    def is_b(self) -> bool:
        return self.value == "B"
    @property
    def is_c(self) -> bool:
        return self.value == "C"
