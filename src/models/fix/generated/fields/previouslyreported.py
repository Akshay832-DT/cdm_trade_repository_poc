"""
FIX PreviouslyReported field (tag 570).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PreviouslyReportedValues:
    """Enumerated values for PreviouslyReported."""
    Y = "Y"  # YES
    N = "N"  # NO

class PreviouslyReportedField(FIXFieldBase):
    """"""
    tag: str = "570"
    name: str = "PreviouslyReported"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
