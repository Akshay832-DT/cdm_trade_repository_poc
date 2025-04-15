"""
FIX Scope field (tag 546).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ScopeValues:
    """Enumerated values for Scope."""
    VALUE_1 = "1"  # LOCAL_MARKET
    VALUE_2 = "2"  # NATIONAL
    VALUE_3 = "3"  # GLOBAL

class ScopeField(FIXFieldBase):
    """"""
    tag: str = "546"
    name: str = "Scope"
    type: str = "MULTIPLEVALUESTRING"
    value: List[str]

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
