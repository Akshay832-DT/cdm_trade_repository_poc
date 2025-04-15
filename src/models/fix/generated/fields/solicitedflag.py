"""
FIX SolicitedFlag field (tag 377).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SolicitedFlagValues:
    """Enumerated values for SolicitedFlag."""
    Y = "Y"  # YES
    N = "N"  # NO

class SolicitedFlagField(FIXFieldBase):
    """"""
    tag: str = "377"
    name: str = "SolicitedFlag"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
