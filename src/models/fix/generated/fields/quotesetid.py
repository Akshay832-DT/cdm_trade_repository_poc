
from .base import FIXFieldBase
from .types import FIXString

class QuoteSetID(FIXFieldBase):
    """FIX QuoteSetID field."""
    tag: str = "302"
    name: str = "QuoteSetID"
    type: str = "STRING"
    value: FIXString
