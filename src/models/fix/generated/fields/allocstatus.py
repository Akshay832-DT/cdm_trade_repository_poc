"""
FIX AllocStatus field (tag 87).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocStatusValues:
    """Enumerated values for AllocStatus."""
    VALUE_0 = "0"  # ACCEPTED
    VALUE_1 = "1"  # BLOCK_LEVEL_REJECT
    VALUE_2 = "2"  # ACCOUNT_LEVEL_REJECT
    VALUE_3 = "3"  # RECEIVED
    VALUE_4 = "4"  # INCOMPLETE
    VALUE_5 = "5"  # REJECTED_BY_INTERMEDIARY

class AllocStatusField(FIXFieldBase):
    """"""
    tag: str = "87"
    name: str = "AllocStatus"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "5"]

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
