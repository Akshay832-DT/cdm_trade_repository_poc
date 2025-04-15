"""
FIX TradeAllocIndicator field (tag 826).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeAllocIndicatorValues:
    """Enumerated values for TradeAllocIndicator."""
    VALUE_0 = "0"  # ALLOCATION_NOT_REQUIRED
    VALUE_1 = "1"  # ALLOCATION_REQUIRED
    VALUE_2 = "2"  # USE_ALLOCATION_PROVIDED_WITH_THE_TRADE

class TradeAllocIndicatorField(FIXFieldBase):
    """"""
    tag: str = "826"
    name: str = "TradeAllocIndicator"
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
