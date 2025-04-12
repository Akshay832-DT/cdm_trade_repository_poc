
from .base import FIXFieldBase
from .types import FIXString

class SecondaryAllocID(FIXFieldBase):
    """FIX SecondaryAllocID field."""
    tag: str = "793"
    name: str = "SecondaryAllocID"
    type: str = "STRING"
    value: FIXString
