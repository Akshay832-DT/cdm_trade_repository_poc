
from .base import FIXFieldBase
from .types import FIXString

class BeginString(FIXFieldBase):
    """FIX BeginString field."""
    tag: str = "8"
    name: str = "BeginString"
    type: str = "STRING"
    value: FIXString
