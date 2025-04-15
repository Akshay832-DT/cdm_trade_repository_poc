"""
FIX TrdType field (tag 828).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TrdTypeValues:
    """Enumerated values for TrdType."""
    VALUE_0 = "0"  # REGULAR_TRADE
    VALUE_1 = "1"  # BLOCK_TRADE
    VALUE_2 = "2"  # EFP
    VALUE_3 = "3"  # TRANSFER
    VALUE_4 = "4"  # LATE_TRADE
    VALUE_5 = "5"  # T_TRADE
    VALUE_6 = "6"  # WEIGHTED_AVERAGE_PRICE_TRADE
    VALUE_7 = "7"  # BUNCHED_TRADE
    VALUE_8 = "8"  # LATE_BUNCHED_TRADE
    VALUE_9 = "9"  # PRIOR_REFERENCE_PRICE_TRADE
    VALUE_10 = "10"  # AFTER_HOURS_TRADE

class TrdTypeField(FIXFieldBase):
    """"""
    tag: str = "828"
    name: str = "TrdType"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

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
    @property
    def is_value_7(self) -> bool:
        return self.value == "7"
    @property
    def is_value_8(self) -> bool:
        return self.value == "8"
    @property
    def is_value_9(self) -> bool:
        return self.value == "9"
    @property
    def is_value_10(self) -> bool:
        return self.value == "10"
