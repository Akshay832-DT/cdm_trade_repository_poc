"""
FIX IOINaturalFlag field (tag 130).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class IOINaturalFlagValues:
    """Enumerated values for IOINaturalFlag."""
    Y = "Y"  # YES
    N = "N"  # NO

class IOINaturalFlagField(FIXFieldBase):
    """"""
    tag: str = "130"
    name: str = "IOINaturalFlag"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
