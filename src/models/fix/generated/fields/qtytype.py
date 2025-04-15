"""
FIX QtyType field (tag 854).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QtyTypeValues:
    """Enumerated values for QtyType."""
    VALUE_0 = "0"  # UNITS
    VALUE_1 = "1"  # CONTRACTS

class QtyTypeField(FIXFieldBase):
    """"""
    tag: str = "854"
    name: str = "QtyType"
    type: str = "INT"
    value: Literal["0", "1"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
