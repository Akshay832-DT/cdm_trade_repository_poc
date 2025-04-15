"""
FIX MDUpdateAction field (tag 279).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDUpdateActionValues:
    """Enumerated values for MDUpdateAction."""
    VALUE_0 = "0"  # NEW
    VALUE_1 = "1"  # CHANGE
    VALUE_2 = "2"  # DELETE

class MDUpdateActionField(FIXFieldBase):
    """"""
    tag: str = "279"
    name: str = "MDUpdateAction"
    type: str = "CHAR"
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
