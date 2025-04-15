"""
FIX PositionEffect field (tag 77).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PositionEffectValues:
    """Enumerated values for PositionEffect."""
    O = "O"  # OPEN
    C = "C"  # CLOSE
    R = "R"  # ROLLED
    F = "F"  # FIFO

class PositionEffectField(FIXFieldBase):
    """"""
    tag: str = "77"
    name: str = "PositionEffect"
    type: str = "CHAR"
    value: Literal["O", "C", "R", "F"]

    # Helper methods for enum values
    @property
    def is_o(self) -> bool:
        return self.value == "O"
    @property
    def is_c(self) -> bool:
        return self.value == "C"
    @property
    def is_r(self) -> bool:
        return self.value == "R"
    @property
    def is_f(self) -> bool:
        return self.value == "F"
