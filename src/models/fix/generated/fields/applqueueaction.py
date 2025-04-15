"""
FIX ApplQueueAction field (tag 815).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ApplQueueActionValues:
    """Enumerated values for ApplQueueAction."""
    VALUE_0 = "0"  # NO_ACTION_TAKEN
    VALUE_1 = "1"  # QUEUE_FLUSHED
    VALUE_2 = "2"  # OVERLAY_LAST
    VALUE_3 = "3"  # END_SESSION

class ApplQueueActionField(FIXFieldBase):
    """"""
    tag: str = "815"
    name: str = "ApplQueueAction"
    type: str = "INT"
    value: Literal["0", "1", "2", "3"]

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
    @property
    def is_value_3(self) -> bool:
        return self.value == "3"
