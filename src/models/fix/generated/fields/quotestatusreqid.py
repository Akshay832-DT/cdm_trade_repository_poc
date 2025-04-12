
from .base import FIXFieldBase
from .types import FIXString

class QuoteStatusReqID(FIXFieldBase):
    """FIX QuoteStatusReqID field."""
    tag: str = "649"
    name: str = "QuoteStatusReqID"
    type: str = "STRING"
    value: FIXString
