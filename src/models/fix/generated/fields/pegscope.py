"""
FIX PegScope field (tag 840).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PegScopeValues:
    """Enumerated values for PegScope."""
    VALUE_1 = "1"  # LOCAL
    VALUE_2 = "2"  # NATIONAL
    VALUE_3 = "3"  # GLOBAL
    VALUE_4 = "4"  # NATIONAL_EXCLUDING_LOCAL

class PegScopeField(FIXFieldBase):
    """"""
    tag: str = "840"
    name: str = "PegScope"
    type: str = "INT"
    value: Literal["1", "2", "3", "4"]

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
