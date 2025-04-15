"""
FIX PegRoundDirection field (tag 838).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PegRoundDirectionValues:
    """Enumerated values for PegRoundDirection."""
    VALUE_1 = "1"  # MORE_AGGRESSIVE
    VALUE_2 = "2"  # MORE_PASSIVE

class PegRoundDirectionField(FIXFieldBase):
    """"""
    tag: str = "838"
    name: str = "PegRoundDirection"
    type: str = "INT"
    value: Literal["1", "2"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
