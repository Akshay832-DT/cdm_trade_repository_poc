"""
FIX DiscretionOffsetType field (tag 842).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DiscretionOffsetTypeValues:
    """Enumerated values for DiscretionOffsetType."""
    VALUE_0 = "0"  # PRICE
    VALUE_1 = "1"  # BASIS_POINTS
    VALUE_2 = "2"  # TICKS
    VALUE_3 = "3"  # PRICE_TIER

class DiscretionOffsetTypeField(FIXFieldBase):
    """"""
    tag: str = "842"
    name: str = "DiscretionOffsetType"
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
