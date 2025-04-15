"""
FIX ExchangeForPhysical field (tag 411).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ExchangeForPhysicalValues:
    """Enumerated values for ExchangeForPhysical."""
    Y = "Y"  # YES
    N = "N"  # NO

class ExchangeForPhysicalField(FIXFieldBase):
    """"""
    tag: str = "411"
    name: str = "ExchangeForPhysical"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
