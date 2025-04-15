"""
FIX DiscretionScope field (tag 846).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DiscretionScopeValues:
    """Enumerated values for DiscretionScope."""
    VALUE_1 = "1"  # LOCAL
    VALUE_2 = "2"  # NATIONAL
    VALUE_3 = "3"  # GLOBAL
    VALUE_4 = "4"  # NATIONAL_EXCLUDING_LOCAL

class DiscretionScopeField(FIXFieldBase):
    """"""
    tag: str = "846"
    name: str = "DiscretionScope"
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
