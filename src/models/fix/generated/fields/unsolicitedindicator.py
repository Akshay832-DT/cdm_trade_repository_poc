"""
FIX UnsolicitedIndicator field (tag 325).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnsolicitedIndicatorValues:
    """Enumerated values for UnsolicitedIndicator."""
    Y = "Y"  # YES
    N = "N"  # NO

class UnsolicitedIndicatorField(FIXFieldBase):
    """"""
    tag: str = "325"
    name: str = "UnsolicitedIndicator"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
