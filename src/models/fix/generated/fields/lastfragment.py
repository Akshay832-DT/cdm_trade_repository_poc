"""
FIX LastFragment field (tag 893).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LastFragmentValues:
    """Enumerated values for LastFragment."""
    Y = "Y"  # YES
    N = "N"  # NO

class LastFragmentField(FIXFieldBase):
    """"""
    tag: str = "893"
    name: str = "LastFragment"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
