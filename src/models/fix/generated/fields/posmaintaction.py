"""
FIX PosMaintAction field (tag 712).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PosMaintActionValues:
    """Enumerated values for PosMaintAction."""
    VALUE_1 = "1"  # NEW
    VALUE_2 = "2"  # REPLACE
    VALUE_3 = "3"  # CANCEL

class PosMaintActionField(FIXFieldBase):
    """"""
    tag: str = "712"
    name: str = "PosMaintAction"
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
