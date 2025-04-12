
from .base import FIXFieldBase
from .types import FIXString

class QuoteID(FIXFieldBase):
    """FIX QuoteID field."""
    tag: str = "117"
    name: str = "QuoteID"
    type: str = "STRING"
    value: FIXString
