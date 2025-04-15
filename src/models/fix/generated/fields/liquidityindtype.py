"""
FIX LiquidityIndType field (tag 409).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LiquidityIndTypeValues:
    """Enumerated values for LiquidityIndType."""
    VALUE_1 = "1"  # FIVE_DAY_MOVING_AVERAGE
    VALUE_2 = "2"  # TWENTY_DAY_MOVING_AVERAGE
    VALUE_3 = "3"  # NORMAL_MARKET_SIZE
    VALUE_4 = "4"  # OTHER

class LiquidityIndTypeField(FIXFieldBase):
    """"""
    tag: str = "409"
    name: str = "LiquidityIndType"
    type: str = "INT"
    value: Literal["1", "2", "3", "4"]

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
    @property
    def is_value_4(self) -> bool:
        return self.value == "4"
