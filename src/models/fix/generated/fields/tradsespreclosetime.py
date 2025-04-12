
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class TradSesPreCloseTime(FIXFieldBase):
    """FIX TradSesPreCloseTime field."""
    tag: str = "343"
    name: str = "TradSesPreCloseTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
