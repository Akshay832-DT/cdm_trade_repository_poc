"""
FIX IOIQltyInd field (tag 25).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class IOIQltyIndValues:
    """Enumerated values for IOIQltyInd."""
    L = "L"  # LOW
    M = "M"  # MEDIUM
    H = "H"  # HIGH

class IOIQltyIndField(FIXFieldBase):
    """"""
    tag: str = "25"
    name: str = "IOIQltyInd"
    type: str = "CHAR"
    value: Literal["L", "M", "H"]

    # Helper methods for enum values
    @property
    def is_l(self) -> bool:
        return self.value == "L"
    @property
    def is_m(self) -> bool:
        return self.value == "M"
    @property
    def is_h(self) -> bool:
        return self.value == "H"
