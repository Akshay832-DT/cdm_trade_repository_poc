
from .base import FIXFieldBase
from .types import FIXChar

class LegSide(FIXFieldBase):
    """FIX LegSide field."""
    tag: str = "624"
    name: str = "LegSide"
    type: str = "CHAR"
    value: FIXChar
