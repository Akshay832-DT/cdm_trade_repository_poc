"""
FIX AdvTransType field (tag 5).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AdvTransTypeValues:
    """Enumerated values for AdvTransType."""
    N = "N"  # NEW
    C = "C"  # CANCEL
    R = "R"  # REPLACE

class AdvTransTypeField(FIXFieldBase):
    """"""
    tag: str = "5"
    name: str = "AdvTransType"
    type: str = "STRING"
    value: Literal["N", "C", "R"]

    # Helper methods for enum values
    @property
    def is_n(self) -> bool:
        return self.value == "N"
    @property
    def is_c(self) -> bool:
        return self.value == "C"
    @property
    def is_r(self) -> bool:
        return self.value == "R"
