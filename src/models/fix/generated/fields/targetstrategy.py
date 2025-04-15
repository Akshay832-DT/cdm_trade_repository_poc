"""
FIX TargetStrategy field (tag 847).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TargetStrategyValues:
    """Enumerated values for TargetStrategy."""
    VALUE_1 = "1"  # VWAP
    VALUE_2 = "2"  # PARTICIPATE
    VALUE_3 = "3"  # MININIZE_MARKET_IMPACT

class TargetStrategyField(FIXFieldBase):
    """"""
    tag: str = "847"
    name: str = "TargetStrategy"
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
