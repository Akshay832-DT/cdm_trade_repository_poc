"""
FIX SettlPriceType field (tag 731).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlPriceTypeValues:
    """Enumerated values for SettlPriceType."""
    VALUE_1 = "1"  # FINAL
    VALUE_2 = "2"  # THEORETICAL

class SettlPriceTypeField(FIXFieldBase):
    """"""
    tag: str = "731"
    name: str = "SettlPriceType"
    type: str = "INT"
    value: Literal["1", "2"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
