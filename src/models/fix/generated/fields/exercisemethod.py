"""
FIX ExerciseMethod field (tag 747).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ExerciseMethodValues:
    """Enumerated values for ExerciseMethod."""
    A = "A"  # AUTOMATIC
    M = "M"  # MANUAL

class ExerciseMethodField(FIXFieldBase):
    """"""
    tag: str = "747"
    name: str = "ExerciseMethod"
    type: str = "CHAR"
    value: Literal["A", "M"]

    # Helper methods for enum values
    @property
    def is_a(self) -> bool:
        return self.value == "A"
    @property
    def is_m(self) -> bool:
        return self.value == "M"
