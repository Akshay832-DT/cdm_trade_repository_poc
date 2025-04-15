"""
FIX PossDupFlag field (tag 43).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PossDupFlagValues:
    """Enumerated values for PossDupFlag."""
    Y = "Y"  # YES
    N = "N"  # NO

class PossDupFlagField(FIXFieldBase):
    """"""
    tag: str = "43"
    name: str = "PossDupFlag"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
