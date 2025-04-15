"""
FIX CollAction field (tag 944).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CollActionValues:
    """Enumerated values for CollAction."""
    VALUE_0 = "0"  # RETAIN
    VALUE_1 = "1"  # ADD
    VALUE_2 = "2"  # REMOVE

class CollActionField(FIXFieldBase):
    """"""
    tag: str = "944"
    name: str = "CollAction"
    type: str = "INT"
    value: Literal["0", "1", "2"]

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
