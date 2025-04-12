
from .base import FIXFieldBase
from .types import FIXString

class SecondaryExecID(FIXFieldBase):
    """FIX SecondaryExecID field."""
    tag: str = "527"
    name: str = "SecondaryExecID"
    type: str = "STRING"
    value: FIXString
