"""
FIX AllocTransType field (tag 71).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocTransTypeValues:
    """Enumerated values for AllocTransType."""
    VALUE_0 = "0"  # NEW
    VALUE_1 = "1"  # REPLACE
    VALUE_2 = "2"  # CANCEL

class AllocTransTypeField(FIXFieldBase):
    """"""
    tag: str = "71"
    name: str = "AllocTransType"
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
