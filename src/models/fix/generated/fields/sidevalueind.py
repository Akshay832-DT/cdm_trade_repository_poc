"""
FIX SideValueInd field (tag 401).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SideValueIndValues:
    """Enumerated values for SideValueInd."""
    VALUE_1 = "1"  # SIDE_VALUE1
    VALUE_2 = "2"  # SIDE_VALUE2

class SideValueIndField(FIXFieldBase):
    """"""
    tag: str = "401"
    name: str = "SideValueInd"
    type: str = "INT"
    value: Literal["1", "2"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
