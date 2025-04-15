"""
FIX RoundingDirection field (tag 468).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RoundingDirectionValues:
    """Enumerated values for RoundingDirection."""
    VALUE_0 = "0"  # ROUND_TO_NEAREST
    VALUE_1 = "1"  # ROUND_DOWN
    VALUE_2 = "2"  # ROUND_UP

class RoundingDirectionField(FIXFieldBase):
    """"""
    tag: str = "468"
    name: str = "RoundingDirection"
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
