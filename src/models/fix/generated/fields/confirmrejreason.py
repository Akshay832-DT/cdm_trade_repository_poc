"""
FIX ConfirmRejReason field (tag 774).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ConfirmRejReasonValues:
    """Enumerated values for ConfirmRejReason."""
    VALUE_1 = "1"  # MISMATCHED_ACCOUNT
    VALUE_2 = "2"  # MISSING_SETTLEMENT_INSTRUCTIONS
    VALUE_99 = "99"  # OTHER

class ConfirmRejReasonField(FIXFieldBase):
    """"""
    tag: str = "774"
    name: str = "ConfirmRejReason"
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
