"""
FIX IOITransType field (tag 28).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class IOITransTypeValues:
    """Enumerated values for IOITransType."""
    N = "N"  # NEW
    C = "C"  # CANCEL
    R = "R"  # REPLACE

class IOITransTypeField(FIXFieldBase):
    """"""
    tag: str = "28"
    name: str = "IOITransType"
    type: str = "CHAR"
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
