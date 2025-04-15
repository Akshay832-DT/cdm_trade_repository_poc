"""
FIX IOIQty field (tag 27).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class IOIQtyValues:
    """Enumerated values for IOIQty."""
    S = "S"  # SMALL
    M = "M"  # MEDIUM
    L = "L"  # LARGE

class IOIQtyField(FIXFieldBase):
    """"""
    tag: str = "27"
    name: str = "IOIQty"
    type: str = "STRING"
    value: Literal["S", "M", "L"]

    # Helper methods for enum values
    @property
    def is_s(self) -> bool:
        return self.value == "S"
    @property
    def is_m(self) -> bool:
        return self.value == "M"
    @property
    def is_l(self) -> bool:
        return self.value == "L"
