
from .base import FIXFieldBase
from .types import FIXString

class TradeRequestID(FIXFieldBase):
    """FIX TradeRequestID field."""
    tag: str = "568"
    name: str = "TradeRequestID"
    type: str = "STRING"
    value: FIXString
