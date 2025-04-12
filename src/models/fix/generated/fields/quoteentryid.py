
from .base import FIXFieldBase
from .types import FIXString

class QuoteEntryID(FIXFieldBase):
    """FIX QuoteEntryID field."""
    tag: str = "299"
    name: str = "QuoteEntryID"
    type: str = "STRING"
    value: FIXString
