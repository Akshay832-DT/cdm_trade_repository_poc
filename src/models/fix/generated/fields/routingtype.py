"""
FIX RoutingType field (tag 216).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RoutingTypeValues:
    """Enumerated values for RoutingType."""
    VALUE_1 = "1"  # TARGET_FIRM
    VALUE_2 = "2"  # TARGET_LIST
    VALUE_3 = "3"  # BLOCK_FIRM
    VALUE_4 = "4"  # BLOCK_LIST

class RoutingTypeField(FIXFieldBase):
    """"""
    tag: str = "216"
    name: str = "RoutingType"
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
