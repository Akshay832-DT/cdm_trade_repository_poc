"""
FIX TerminationType field (tag 788).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TerminationTypeValues:
    """Enumerated values for TerminationType."""
    VALUE_1 = "1"  # OVERNIGHT
    VALUE_2 = "2"  # TERM
    VALUE_3 = "3"  # FLEXIBLE
    VALUE_4 = "4"  # OPEN

class TerminationTypeField(FIXFieldBase):
    """"""
    tag: str = "788"
    name: str = "TerminationType"
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
