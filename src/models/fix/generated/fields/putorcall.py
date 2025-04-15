"""
FIX PutOrCall field (tag 201).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PutOrCallValues:
    """Enumerated values for PutOrCall."""
    VALUE_0 = "0"  # PUT
    VALUE_1 = "1"  # CALL

class PutOrCallField(FIXFieldBase):
    """"""
    tag: str = "201"
    name: str = "PutOrCall"
    type: str = "INT"
    value: Literal["0", "1"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
