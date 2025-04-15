"""
FIX PossResend field (tag 97).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PossResendValues:
    """Enumerated values for PossResend."""
    Y = "Y"  # YES
    N = "N"  # NO

class PossResendField(FIXFieldBase):
    """"""
    tag: str = "97"
    name: str = "PossResend"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
