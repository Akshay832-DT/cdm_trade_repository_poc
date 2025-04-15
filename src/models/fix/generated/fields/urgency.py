"""
FIX Urgency field (tag 61).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UrgencyValues:
    """Enumerated values for Urgency."""
    VALUE_0 = "0"  # NORMAL
    VALUE_1 = "1"  # FLASH
    VALUE_2 = "2"  # BACKGROUND

class UrgencyField(FIXFieldBase):
    """"""
    tag: str = "61"
    name: str = "Urgency"
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
