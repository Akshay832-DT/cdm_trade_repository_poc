"""
FIX HandlInst field (tag 21).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class HandlInstValues:
    """Enumerated values for HandlInst."""
    VALUE_1 = "1"  # AUTOMATED_EXECUTION_NO_INTERVENTION
    VALUE_2 = "2"  # AUTOMATED_EXECUTION_INTERVENTION_OK
    VALUE_3 = "3"  # MANUAL_ORDER

class HandlInstField(FIXFieldBase):
    """"""
    tag: str = "21"
    name: str = "HandlInst"
    type: str = "CHAR"
    value: Literal["1", "2", "3"]

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
