"""
FIX EmailType field (tag 94).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EmailTypeValues:
    """Enumerated values for EmailType."""
    VALUE_0 = "0"  # NEW
    VALUE_1 = "1"  # REPLY
    VALUE_2 = "2"  # ADMIN_REPLY

class EmailTypeField(FIXFieldBase):
    """"""
    tag: str = "94"
    name: str = "EmailType"
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
