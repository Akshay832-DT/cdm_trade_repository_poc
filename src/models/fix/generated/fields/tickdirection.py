"""
FIX TickDirection field (tag 274).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TickDirectionValues:
    """Enumerated values for TickDirection."""
    VALUE_0 = "0"  # PLUS_TICK
    VALUE_1 = "1"  # ZERO_PLUS_TICK
    VALUE_2 = "2"  # MINUS_TICK
    VALUE_3 = "3"  # ZERO_MINUS_TICK

class TickDirectionField(FIXFieldBase):
    """"""
    tag: str = "274"
    name: str = "TickDirection"
    type: str = "CHAR"
    value: Literal["0", "1", "2", "3"]

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
