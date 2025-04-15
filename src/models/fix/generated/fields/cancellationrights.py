"""
FIX CancellationRights field (tag 480).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CancellationRightsValues:
    """Enumerated values for CancellationRights."""
    Y = "Y"  # YES
    N = "N"  # NO_EXECUTION_ONLY
    M = "M"  # NO_WAIVER_AGREEMENT
    O = "O"  # NO_INSTITUTIONAL

class CancellationRightsField(FIXFieldBase):
    """"""
    tag: str = "480"
    name: str = "CancellationRights"
    type: str = "CHAR"
    value: Literal["Y", "N", "M", "O"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
    @property
    def is_m(self) -> bool:
        return self.value == "M"
    @property
    def is_o(self) -> bool:
        return self.value == "O"
