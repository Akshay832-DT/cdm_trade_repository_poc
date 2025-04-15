"""
FIX MatchStatus field (tag 573).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MatchStatusValues:
    """Enumerated values for MatchStatus."""
    VALUE_0 = "0"  # COMPARED
    VALUE_1 = "1"  # UNCOMPARED
    VALUE_2 = "2"  # ADVISORY_OR_ALERT

class MatchStatusField(FIXFieldBase):
    """"""
    tag: str = "573"
    name: str = "MatchStatus"
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
