
from .base import FIXFieldBase
from .types import FIXString

class TradingSessionSubID(FIXFieldBase):
    """FIX TradingSessionSubID field."""
    tag: str = "625"
    name: str = "TradingSessionSubID"
    type: str = "STRING"
    value: FIXString
