
from .base import FIXFieldBase
from .types import FIXString

class MDEntrySeller(FIXFieldBase):
    """FIX MDEntrySeller field."""
    tag: str = "289"
    name: str = "MDEntrySeller"
    type: str = "STRING"
    value: FIXString
