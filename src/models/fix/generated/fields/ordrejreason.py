"""
FIX OrdRejReason field (tag 103).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrdRejReasonValues:
    """Enumerated values for OrdRejReason."""
    VALUE_0 = "0"  # BROKER_CREDIT
    VALUE_1 = "1"  # UNKNOWN_SYMBOL
    VALUE_2 = "2"  # EXCHANGE_CLOSED
    VALUE_3 = "3"  # ORDER_EXCEEDS_LIMIT
    VALUE_4 = "4"  # TOO_LATE_TO_ENTER
    VALUE_5 = "5"  # UNKNOWN_ORDER
    VALUE_6 = "6"  # DUPLICATE_ORDER
    VALUE_7 = "7"  # DUPLICATE_OF_A_VERBALLY_COMMUNICATED_ORDER
    VALUE_8 = "8"  # STALE_ORDER
    VALUE_9 = "9"  # TRADE_ALONG_REQUIRED
    VALUE_10 = "10"  # INVALID_INVESTOR_ID
    VALUE_11 = "11"  # UNSUPPORTED_ORDER_CHARACTERISTIC
    VALUE_13 = "13"  # INCORRECT_QUANTITY
    VALUE_14 = "14"  # INCORRECT_ALLOCATED_QUANTITY
    VALUE_15 = "15"  # UNKNOWN_ACCOUNT
    VALUE_99 = "99"  # OTHER

class OrdRejReasonField(FIXFieldBase):
    """"""
    tag: str = "103"
    name: str = "OrdRejReason"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "13", "14", "15", "99"]

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
    def is_value_13(self) -> bool:
        return self.value == "13"
    @property
    def is_value_14(self) -> bool:
        return self.value == "14"
    @property
    def is_value_15(self) -> bool:
        return self.value == "15"
    @property
    def is_value_99(self) -> bool:
        return self.value == "99"
