
from .base import FIXFieldBase
from .types import FIXString

class TradingSessionID(FIXFieldBase):
    """FIX TradingSessionID field."""
    tag: str = "336"
    name: str = "TradingSessionID"
    type: str = "STRING"
    value: FIXString
