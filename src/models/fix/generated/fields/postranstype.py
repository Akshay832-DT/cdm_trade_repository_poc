"""
FIX PosTransType field (tag 709).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PosTransTypeValues:
    """Enumerated values for PosTransType."""
    VALUE_1 = "1"  # EXERCISE
    VALUE_2 = "2"  # DO_NOT_EXERCISE
    VALUE_3 = "3"  # POSITION_ADJUSTMENT
    VALUE_4 = "4"  # POSITION_CHANGE_SUBMISSION
    VALUE_5 = "5"  # PLEDGE

class PosTransTypeField(FIXFieldBase):
    """"""
    tag: str = "709"
    name: str = "PosTransType"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5"]

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
    @property
    def is_value_5(self) -> bool:
        return self.value == "5"
