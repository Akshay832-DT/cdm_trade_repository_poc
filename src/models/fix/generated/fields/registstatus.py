"""
FIX RegistStatus field (tag 506).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RegistStatusValues:
    """Enumerated values for RegistStatus."""
    A = "A"  # ACCEPTED
    R = "R"  # REJECTED
    H = "H"  # HELD
    N = "N"  # REMINDER

class RegistStatusField(FIXFieldBase):
    """"""
    tag: str = "506"
    name: str = "RegistStatus"
    type: str = "CHAR"
    value: Literal["A", "R", "H", "N"]

    # Helper methods for enum values
    @property
    def is_a(self) -> bool:
        return self.value == "A"
    @property
    def is_r(self) -> bool:
        return self.value == "R"
    @property
    def is_h(self) -> bool:
        return self.value == "H"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
