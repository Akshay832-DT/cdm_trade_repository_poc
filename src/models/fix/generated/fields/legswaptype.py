"""
FIX LegSwapType field (tag 690).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegSwapTypeValues:
    """Enumerated values for LegSwapType."""
    VALUE_1 = "1"  # PAR_FOR_PAR
    VALUE_2 = "2"  # MODIFIED_DURATION
    VALUE_4 = "4"  # RISK
    VALUE_5 = "5"  # PROCEEDS

class LegSwapTypeField(FIXFieldBase):
    """"""
    tag: str = "690"
    name: str = "LegSwapType"
    type: str = "INT"
    value: Literal["1", "2", "4", "5"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
    @property
    def is_value_4(self) -> bool:
        return self.value == "4"
    @property
    def is_value_5(self) -> bool:
        return self.value == "5"
