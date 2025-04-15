"""
FIX PegMoveType field (tag 835).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PegMoveTypeValues:
    """Enumerated values for PegMoveType."""
    VALUE_0 = "0"  # FLOATING
    VALUE_1 = "1"  # FIXED

class PegMoveTypeField(FIXFieldBase):
    """"""
    tag: str = "835"
    name: str = "PegMoveType"
    type: str = "INT"
    value: Literal["0", "1"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
