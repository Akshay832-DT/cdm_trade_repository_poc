"""
FIX PublishTrdIndicator field (tag 852).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PublishTrdIndicatorValues:
    """Enumerated values for PublishTrdIndicator."""
    Y = "Y"  # YES
    N = "N"  # NO

class PublishTrdIndicatorField(FIXFieldBase):
    """"""
    tag: str = "852"
    name: str = "PublishTrdIndicator"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
