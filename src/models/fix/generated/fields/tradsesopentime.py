
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class TradSesOpenTime(FIXFieldBase):
    """FIX TradSesOpenTime field."""
    tag: str = "342"
    name: str = "TradSesOpenTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
