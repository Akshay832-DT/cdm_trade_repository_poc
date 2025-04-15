"""
FIX ConfirmType field (tag 773).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ConfirmTypeValues:
    """Enumerated values for ConfirmType."""
    VALUE_1 = "1"  # STATUS
    VALUE_2 = "2"  # CONFIRMATION
    VALUE_3 = "3"  # CONFIRMATION_REQUEST_REJECTED

class ConfirmTypeField(FIXFieldBase):
    """"""
    tag: str = "773"
    name: str = "ConfirmType"
    type: str = "INT"
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
