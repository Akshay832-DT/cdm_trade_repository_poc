"""
FIX DiscretionMoveType field (tag 841).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DiscretionMoveTypeValues:
    """Enumerated values for DiscretionMoveType."""
    VALUE_0 = "0"  # FLOATING
    VALUE_1 = "1"  # FIXED

class DiscretionMoveTypeField(FIXFieldBase):
    """"""
    tag: str = "841"
    name: str = "DiscretionMoveType"
    type: str = "INT"
    value: Literal["0", "1"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
