"""
FIX SettlInstTransType field (tag 163).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlInstTransTypeValues:
    """Enumerated values for SettlInstTransType."""
    N = "N"  # NEW
    C = "C"  # CANCEL
    R = "R"  # REPLACE
    T = "T"  # RESTATE

class SettlInstTransTypeField(FIXFieldBase):
    """"""
    tag: str = "163"
    name: str = "SettlInstTransType"
    type: str = "CHAR"
    value: Literal["N", "C", "R", "T"]

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
    @property
    def is_t(self) -> bool:
        return self.value == "T"
