"""
FIX OddLot field (tag 575).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OddLotValues:
    """Enumerated values for OddLot."""
    Y = "Y"  # YES
    N = "N"  # NO

class OddLotField(FIXFieldBase):
    """"""
    tag: str = "575"
    name: str = "OddLot"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
