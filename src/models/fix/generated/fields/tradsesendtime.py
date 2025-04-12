
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class TradSesEndTime(FIXFieldBase):
    """FIX TradSesEndTime field."""
    tag: str = "345"
    name: str = "TradSesEndTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
