"""
FIX DueToRelated field (tag 329).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DueToRelatedValues:
    """Enumerated values for DueToRelated."""
    Y = "Y"  # YES
    N = "N"  # NO

class DueToRelatedField(FIXFieldBase):
    """"""
    tag: str = "329"
    name: str = "DueToRelated"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
