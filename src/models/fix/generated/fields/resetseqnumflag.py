"""
FIX ResetSeqNumFlag field (tag 141).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ResetSeqNumFlagValues:
    """Enumerated values for ResetSeqNumFlag."""
    Y = "Y"  # YES
    N = "N"  # NO

class ResetSeqNumFlagField(FIXFieldBase):
    """"""
    tag: str = "141"
    name: str = "ResetSeqNumFlag"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
