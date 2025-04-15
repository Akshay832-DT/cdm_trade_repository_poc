"""
FIX NetworkRequestType field (tag 935).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NetworkRequestTypeValues:
    """Enumerated values for NetworkRequestType."""
    VALUE_1 = "1"  # SNAPSHOT
    VALUE_2 = "2"  # SUBSCRIBE
    VALUE_4 = "4"  # STOP_SUBSCRIBING
    VALUE_8 = "8"  # LEVEL_OF_DETAIL

class NetworkRequestTypeField(FIXFieldBase):
    """"""
    tag: str = "935"
    name: str = "NetworkRequestType"
    type: str = "INT"
    value: Literal["1", "2", "4", "8"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
    @property
    def is_value_4(self) -> bool:
        return self.value == "4"
    @property
    def is_value_8(self) -> bool:
        return self.value == "8"
