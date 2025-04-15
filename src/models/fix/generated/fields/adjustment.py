"""
FIX Adjustment field (tag 334).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AdjustmentValues:
    """Enumerated values for Adjustment."""
    VALUE_1 = "1"  # CANCEL
    VALUE_2 = "2"  # ERROR
    VALUE_3 = "3"  # CORRECTION

class AdjustmentField(FIXFieldBase):
    """"""
    tag: str = "334"
    name: str = "Adjustment"
    type: str = "INT"
    value: Literal["1", "2", "3"]

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
