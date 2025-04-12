
from .base import FIXFieldBase
from .types import FIXString

class TradeInputSource(FIXFieldBase):
    """FIX TradeInputSource field."""
    tag: str = "578"
    name: str = "TradeInputSource"
    type: str = "STRING"
    value: FIXString
