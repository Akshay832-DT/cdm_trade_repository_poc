"""
FIX CollStatus field (tag 910).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CollStatusValues:
    """Enumerated values for CollStatus."""
    VALUE_0 = "0"  # UNASSIGNED
    VALUE_1 = "1"  # PARTIALLY_ASSIGNED
    VALUE_2 = "2"  # ASSIGNMENT_PROPOSED
    VALUE_3 = "3"  # ASSIGNED
    VALUE_4 = "4"  # CHALLENGED

class CollStatusField(FIXFieldBase):
    """"""
    tag: str = "910"
    name: str = "CollStatus"
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
