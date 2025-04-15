"""
FIX PriorityIndicator field (tag 638).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PriorityIndicatorValues:
    """Enumerated values for PriorityIndicator."""
    VALUE_0 = "0"  # PRIORITY_UNCHANGED
    VALUE_1 = "1"  # LOST_PRIORITY_AS_RESULT_OF_ORDER_CHANGE

class PriorityIndicatorField(FIXFieldBase):
    """"""
    tag: str = "638"
    name: str = "PriorityIndicator"
    type: str = "INT"
    value: Literal["0", "1"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
