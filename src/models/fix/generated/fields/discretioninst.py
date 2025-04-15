"""
FIX DiscretionInst field (tag 388).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DiscretionInstValues:
    """Enumerated values for DiscretionInst."""
    VALUE_0 = "0"  # RELATED_TO_DISPLAYED_PRICE
    VALUE_1 = "1"  # RELATED_TO_MARKET_PRICE
    VALUE_2 = "2"  # RELATED_TO_PRIMARY_PRICE
    VALUE_3 = "3"  # RELATED_TO_LOCAL_PRIMARY_PRICE
    VALUE_4 = "4"  # RELATED_TO_MIDPOINT_PRICE
    VALUE_5 = "5"  # RELATED_TO_LAST_TRADE_PRICE
    VALUE_6 = "6"  # RELATED_TO_VWAP

class DiscretionInstField(FIXFieldBase):
    """"""
    tag: str = "388"
    name: str = "DiscretionInst"
    type: str = "CHAR"
    value: Literal["0", "1", "2", "3", "4", "5", "6"]

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
    @property
    def is_value_4(self) -> bool:
        return self.value == "4"
    @property
    def is_value_5(self) -> bool:
        return self.value == "5"
    @property
    def is_value_6(self) -> bool:
        return self.value == "6"
