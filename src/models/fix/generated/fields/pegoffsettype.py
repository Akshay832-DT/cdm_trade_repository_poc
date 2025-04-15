"""
FIX PegOffsetType field (tag 836).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PegOffsetTypeValues:
    """Enumerated values for PegOffsetType."""
    VALUE_0 = "0"  # PRICE
    VALUE_1 = "1"  # BASIS_POINTS
    VALUE_2 = "2"  # TICKS
    VALUE_3 = "3"  # PRICE_TIER

class PegOffsetTypeField(FIXFieldBase):
    """"""
    tag: str = "836"
    name: str = "PegOffsetType"
    type: str = "INT"
    value: Literal["0", "1", "2", "3"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
    @property
    def is_value_3(self) -> bool:
        return self.value == "3"
