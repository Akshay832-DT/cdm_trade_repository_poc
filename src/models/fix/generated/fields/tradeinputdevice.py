
from .base import FIXFieldBase
from .types import FIXString

class TradeInputDevice(FIXFieldBase):
    """FIX TradeInputDevice field."""
    tag: str = "579"
    name: str = "TradeInputDevice"
    type: str = "STRING"
    value: FIXString
