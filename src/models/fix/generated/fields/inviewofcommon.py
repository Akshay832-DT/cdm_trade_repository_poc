"""
FIX InViewOfCommon field (tag 328).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class InViewOfCommonValues:
    """Enumerated values for InViewOfCommon."""
    Y = "Y"  # YES
    N = "N"  # NO

class InViewOfCommonField(FIXFieldBase):
    """"""
    tag: str = "328"
    name: str = "InViewOfCommon"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
