
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingTradingSessionSubID(FIXFieldBase):
    """FIX UnderlyingTradingSessionSubID field."""
    tag: str = "823"
    name: str = "UnderlyingTradingSessionSubID"
    type: str = "STRING"
    value: FIXString
