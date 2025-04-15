"""
FIX AggregatedBook field (tag 266).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AggregatedBookValues:
    """Enumerated values for AggregatedBook."""
    Y = "Y"  # YES
    N = "N"  # NO

class AggregatedBookField(FIXFieldBase):
    """"""
    tag: str = "266"
    name: str = "AggregatedBook"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
