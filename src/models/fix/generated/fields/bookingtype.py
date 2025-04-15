"""
FIX BookingType field (tag 775).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BookingTypeValues:
    """Enumerated values for BookingType."""
    VALUE_0 = "0"  # REGULAR_BOOKING
    VALUE_1 = "1"  # CFD
    VALUE_2 = "2"  # TOTAL_RETURN_SWAP

class BookingTypeField(FIXFieldBase):
    """"""
    tag: str = "775"
    name: str = "BookingType"
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
