"""
FIX AllocHandlInst field (tag 209).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocHandlInstValues:
    """Enumerated values for AllocHandlInst."""
    VALUE_1 = "1"  # MATCH
    VALUE_2 = "2"  # FORWARD
    VALUE_3 = "3"  # FORWARD_AND_MATCH

class AllocHandlInstField(FIXFieldBase):
    """"""
    tag: str = "209"
    name: str = "AllocHandlInst"
    type: str = "INT"
    value: Literal["1", "2", "3"]

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
