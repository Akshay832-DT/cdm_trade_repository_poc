"""
FIX LastLiquidityInd field (tag 851).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LastLiquidityIndValues:
    """Enumerated values for LastLiquidityInd."""
    VALUE_1 = "1"  # ADDED_LIQUIDITY
    VALUE_2 = "2"  # REMOVED_LIQUIDITY
    VALUE_3 = "3"  # LIQUIDITY_ROUTED_OUT

class LastLiquidityIndField(FIXFieldBase):
    """"""
    tag: str = "851"
    name: str = "LastLiquidityInd"
    type: str = "INT"
    value: Literal["1", "2", "3"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
    @property
    def is_value_3(self) -> bool:
        return self.value == "3"
