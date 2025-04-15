"""
FIX CrossPrioritization field (tag 550).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CrossPrioritizationValues:
    """Enumerated values for CrossPrioritization."""
    VALUE_0 = "0"  # NONE
    VALUE_1 = "1"  # BUY_SIDE_IS_PRIORITIZED
    VALUE_2 = "2"  # SELL_SIDE_IS_PRIORITIZED

class CrossPrioritizationField(FIXFieldBase):
    """"""
    tag: str = "550"
    name: str = "CrossPrioritization"
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
