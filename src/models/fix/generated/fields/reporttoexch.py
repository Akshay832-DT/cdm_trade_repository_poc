"""
FIX ReportToExch field (tag 113).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ReportToExchValues:
    """Enumerated values for ReportToExch."""
    Y = "Y"  # YES
    N = "N"  # NO

class ReportToExchField(FIXFieldBase):
    """"""
    tag: str = "113"
    name: str = "ReportToExch"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
