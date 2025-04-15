"""
FIX GapFillFlag field (tag 123).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class GapFillFlagValues:
    """Enumerated values for GapFillFlag."""
    Y = "Y"  # YES
    N = "N"  # NO

class GapFillFlagField(FIXFieldBase):
    """"""
    tag: str = "123"
    name: str = "GapFillFlag"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
