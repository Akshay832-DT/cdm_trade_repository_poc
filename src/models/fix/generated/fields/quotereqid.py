
from .base import FIXFieldBase
from .types import FIXString

class QuoteReqID(FIXFieldBase):
    """FIX QuoteReqID field."""
    tag: str = "131"
    name: str = "QuoteReqID"
    type: str = "STRING"
    value: FIXString
