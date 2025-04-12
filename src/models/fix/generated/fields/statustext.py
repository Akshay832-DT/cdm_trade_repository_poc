
from .base import FIXFieldBase
from .types import FIXString

class StatusText(FIXFieldBase):
    """FIX StatusText field."""
    tag: str = "929"
    name: str = "StatusText"
    type: str = "STRING"
    value: FIXString
