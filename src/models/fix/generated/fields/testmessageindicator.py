"""
FIX TestMessageIndicator field (tag 464).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TestMessageIndicatorValues:
    """Enumerated values for TestMessageIndicator."""
    Y = "Y"  # YES
    N = "N"  # NO

class TestMessageIndicatorField(FIXFieldBase):
    """"""
    tag: str = "464"
    name: str = "TestMessageIndicator"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
