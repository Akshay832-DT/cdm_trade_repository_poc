
from .base import FIXFieldBase
from .types import FIXString

class ExecID(FIXFieldBase):
    """FIX ExecID field."""
    tag: str = "17"
    name: str = "ExecID"
    type: str = "STRING"
    value: FIXString
