"""
FIX WorkingIndicator field (tag 636).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class WorkingIndicatorValues:
    """Enumerated values for WorkingIndicator."""
    Y = "Y"  # YES
    N = "N"  # NO

class WorkingIndicatorField(FIXFieldBase):
    """"""
    tag: str = "636"
    name: str = "WorkingIndicator"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
