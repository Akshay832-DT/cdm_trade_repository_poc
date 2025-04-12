
from .base import FIXFieldBase
from .types import FIXString

class TimeBracket(FIXFieldBase):
    """FIX TimeBracket field."""
    tag: str = "943"
    name: str = "TimeBracket"
    type: str = "STRING"
    value: FIXString
