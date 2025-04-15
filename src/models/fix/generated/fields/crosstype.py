"""
FIX CrossType field (tag 549).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CrossTypeValues:
    """Enumerated values for CrossType."""
    VALUE_1 = "1"  # CROSS_AON
    VALUE_2 = "2"  # CROSS_IOC
    VALUE_3 = "3"  # CROSS_ONE_SIDE
    VALUE_4 = "4"  # CROSS_SAME_PRICE

class CrossTypeField(FIXFieldBase):
    """"""
    tag: str = "549"
    name: str = "CrossType"
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
