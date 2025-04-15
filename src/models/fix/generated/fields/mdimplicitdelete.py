"""
FIX MDImplicitDelete field (tag 547).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDImplicitDeleteValues:
    """Enumerated values for MDImplicitDelete."""
    Y = "Y"  # YES
    N = "N"  # NO

class MDImplicitDeleteField(FIXFieldBase):
    """"""
    tag: str = "547"
    name: str = "MDImplicitDelete"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
