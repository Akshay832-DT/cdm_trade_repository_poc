
from .base import FIXFieldBase
from .types import FIXString

class TargetSubID(FIXFieldBase):
    """FIX TargetSubID field."""
    tag: str = "57"
    name: str = "TargetSubID"
    type: str = "STRING"
    value: FIXString
