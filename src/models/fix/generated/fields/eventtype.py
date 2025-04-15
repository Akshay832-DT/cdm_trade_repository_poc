"""
FIX EventType field (tag 865).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EventTypeValues:
    """Enumerated values for EventType."""
    VALUE_1 = "1"  # PUT
    VALUE_2 = "2"  # CALL
    VALUE_3 = "3"  # TENDER
    VALUE_4 = "4"  # SINKING_FUND_CALL
    VALUE_99 = "99"  # OTHER

class EventTypeField(FIXFieldBase):
    """"""
    tag: str = "865"
    name: str = "EventType"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "99"]

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
    def is_value_99(self) -> bool:
        return self.value == "99"
