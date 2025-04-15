"""
FIX AllocCancReplaceReason field (tag 796).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocCancReplaceReasonValues:
    """Enumerated values for AllocCancReplaceReason."""
    VALUE_1 = "1"  # ORIGINAL_DETAILS_INCOMPLETE
    VALUE_2 = "2"  # CHANGE_IN_UNDERLYING_ORDER_DETAILS
    VALUE_99 = "99"  # OTHER

class AllocCancReplaceReasonField(FIXFieldBase):
    """"""
    tag: str = "796"
    name: str = "AllocCancReplaceReason"
    type: str = "INT"
    value: Literal["1", "2", "99"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
    @property
    def is_value_99(self) -> bool:
        return self.value == "99"
