"""
FIX NoSides field (tag 552).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoSidesValues:
    """Enumerated values for NoSides."""
    VALUE_1 = "1"  # ONE_SIDE
    VALUE_2 = "2"  # BOTH_SIDES

class NoSidesField(FIXFieldBase):
    """"""
    tag: str = "552"
    name: str = "NoSides"
    type: str = "NUMINGROUP"
    value: Literal["1", "2"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
