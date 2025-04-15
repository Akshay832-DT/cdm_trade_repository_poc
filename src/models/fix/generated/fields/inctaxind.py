"""
FIX IncTaxInd field (tag 416).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class IncTaxIndValues:
    """Enumerated values for IncTaxInd."""
    VALUE_1 = "1"  # NET
    VALUE_2 = "2"  # GROSS

class IncTaxIndField(FIXFieldBase):
    """"""
    tag: str = "416"
    name: str = "IncTaxInd"
    type: str = "INT"
    value: Literal["1", "2"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
