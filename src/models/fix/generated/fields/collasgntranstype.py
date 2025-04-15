"""
FIX CollAsgnTransType field (tag 903).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CollAsgnTransTypeValues:
    """Enumerated values for CollAsgnTransType."""
    VALUE_0 = "0"  # NEW
    VALUE_1 = "1"  # REPLACE
    VALUE_2 = "2"  # CANCEL
    VALUE_3 = "3"  # RELEASE
    VALUE_4 = "4"  # REVERSE

class CollAsgnTransTypeField(FIXFieldBase):
    """"""
    tag: str = "903"
    name: str = "CollAsgnTransType"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4"]

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
