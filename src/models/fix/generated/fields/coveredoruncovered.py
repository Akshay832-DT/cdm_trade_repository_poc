"""
FIX CoveredOrUncovered field (tag 203).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CoveredOrUncoveredValues:
    """Enumerated values for CoveredOrUncovered."""
    VALUE_0 = "0"  # COVERED
    VALUE_1 = "1"  # UNCOVERED

class CoveredOrUncoveredField(FIXFieldBase):
    """"""
    tag: str = "203"
    name: str = "CoveredOrUncovered"
    type: str = "INT"
    value: Literal["0", "1"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
