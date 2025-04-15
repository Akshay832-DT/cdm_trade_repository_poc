"""
FIX GTBookingInst field (tag 427).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class GTBookingInstValues:
    """Enumerated values for GTBookingInst."""
    VALUE_0 = "0"  # BOOK_OUT_ALL_TRADES_ON_DAY_OF_EXECUTION
    VALUE_1 = "1"  # ACCUMULATE_UNTIL_FILLED_OR_EXPIRED
    VALUE_2 = "2"  # ACCUMULATE_UNTIL_VERBALLLY_NOTIFIED_OTHERWISE

class GTBookingInstField(FIXFieldBase):
    """"""
    tag: str = "427"
    name: str = "GTBookingInst"
    type: str = "INT"
    value: Literal["0", "1", "2"]

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
