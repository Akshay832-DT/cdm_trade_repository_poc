"""
FIX AvgPxIndicator field (tag 819).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AvgPxIndicatorValues:
    """Enumerated values for AvgPxIndicator."""
    VALUE_0 = "0"  # NO_AVERAGE_PRICING
    VALUE_1 = "1"  # TRADE
    VALUE_2 = "2"  # LAST_TRADE

class AvgPxIndicatorField(FIXFieldBase):
    """"""
    tag: str = "819"
    name: str = "AvgPxIndicator"
    type: str = "INT"
    value: Literal["0", "1", "2"]

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
