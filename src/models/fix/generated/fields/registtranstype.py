"""
FIX RegistTransType field (tag 514).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RegistTransTypeValues:
    """Enumerated values for RegistTransType."""
    VALUE_0 = "0"  # NEW
    VALUE_1 = "1"  # REPLACE
    VALUE_2 = "2"  # CANCEL

class RegistTransTypeField(FIXFieldBase):
    """"""
    tag: str = "514"
    name: str = "RegistTransType"
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
