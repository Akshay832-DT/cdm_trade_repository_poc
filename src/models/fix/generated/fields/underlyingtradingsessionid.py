
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingTradingSessionID(FIXFieldBase):
    """FIX UnderlyingTradingSessionID field."""
    tag: str = "822"
    name: str = "UnderlyingTradingSessionID"
    type: str = "STRING"
    value: FIXString
