"""
FIX DayBookingInst field (tag 589).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DayBookingInstValues:
    """Enumerated values for DayBookingInst."""
    VALUE_0 = "0"  # AUTO
    VALUE_1 = "1"  # SPEAK_WITH_ORDER_INITIATOR_BEFORE_BOOKING
    VALUE_2 = "2"  # ACCUMULATE

class DayBookingInstField(FIXFieldBase):
    """"""
    tag: str = "589"
    name: str = "DayBookingInst"
    type: str = "CHAR"
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
