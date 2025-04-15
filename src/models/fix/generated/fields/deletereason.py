"""
FIX DeleteReason field (tag 285).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DeleteReasonValues:
    """Enumerated values for DeleteReason."""
    VALUE_0 = "0"  # CANCELLATION
    VALUE_1 = "1"  # ERROR

class DeleteReasonField(FIXFieldBase):
    """"""
    tag: str = "285"
    name: str = "DeleteReason"
    type: str = "CHAR"
    value: Literal["0", "1"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
