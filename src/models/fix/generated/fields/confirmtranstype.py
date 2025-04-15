"""
FIX ConfirmTransType field (tag 666).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ConfirmTransTypeValues:
    """Enumerated values for ConfirmTransType."""
    VALUE_0 = "0"  # NEW
    VALUE_1 = "1"  # REPLACE
    VALUE_2 = "2"  # CANCEL

class ConfirmTransTypeField(FIXFieldBase):
    """"""
    tag: str = "666"
    name: str = "ConfirmTransType"
    type: str = "INT"
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
