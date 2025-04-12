
from .base import FIXFieldBase
from .types import FIXString

class MDEntryID(FIXFieldBase):
    """FIX MDEntryID field."""
    tag: str = "278"
    name: str = "MDEntryID"
    type: str = "STRING"
    value: FIXString
