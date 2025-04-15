"""
FIX LegalConfirm field (tag 650).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegalConfirmValues:
    """Enumerated values for LegalConfirm."""
    Y = "Y"  # YES
    N = "N"  # NO

class LegalConfirmField(FIXFieldBase):
    """"""
    tag: str = "650"
    name: str = "LegalConfirm"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
