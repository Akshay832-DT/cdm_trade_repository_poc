"""
FIX AdvSide field (tag 4).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AdvSideValues:
    """Enumerated values for AdvSide."""
    B = "B"  # BUY
    S = "S"  # SELL
    X = "X"  # CROSS
    T = "T"  # TRADE

class AdvSideField(FIXFieldBase):
    """"""
    tag: str = "4"
    name: str = "AdvSide"
    type: str = "CHAR"
    value: Literal["B", "S", "X", "T"]

    # Helper methods for enum values
    @property
    def is_b(self) -> bool:
        return self.value == "B"
    @property
    def is_s(self) -> bool:
        return self.value == "S"
    @property
    def is_x(self) -> bool:
        return self.value == "X"
    @property
    def is_t(self) -> bool:
        return self.value == "T"
