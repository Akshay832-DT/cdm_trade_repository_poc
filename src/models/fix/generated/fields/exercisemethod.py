
from .base import FIXFieldBase
from .types import FIXChar

class ExerciseMethod(FIXFieldBase):
    """FIX ExerciseMethod field."""
    tag: str = "747"
    name: str = "ExerciseMethod"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # A: AUTOMATIC
    # M: MANUAL
