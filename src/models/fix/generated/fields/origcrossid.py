
from .base import FIXFieldBase
from .types import FIXString

class OrigCrossID(FIXFieldBase):
    """FIX OrigCrossID field."""
    tag: str = "551"
    name: str = "OrigCrossID"
    type: str = "STRING"
    value: FIXString
