
from .base import FIXFieldBase
from .types import FIXString

class TargetCompID(FIXFieldBase):
    """FIX TargetCompID field."""
    tag: str = "56"
    name: str = "TargetCompID"
    type: str = "STRING"
    value: FIXString
