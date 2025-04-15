"""
FIX ApplQueueResolution field (tag 814).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ApplQueueResolutionValues:
    """Enumerated values for ApplQueueResolution."""
    VALUE_0 = "0"  # NO_ACTION_TAKEN
    VALUE_1 = "1"  # QUEUE_FLUSHED
    VALUE_2 = "2"  # OVERLAY_LAST
    VALUE_3 = "3"  # END_SESSION

class ApplQueueResolutionField(FIXFieldBase):
    """"""
    tag: str = "814"
    name: str = "ApplQueueResolution"
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
