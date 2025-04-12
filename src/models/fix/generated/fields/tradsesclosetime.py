
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class TradSesCloseTime(FIXFieldBase):
    """FIX TradSesCloseTime field."""
    tag: str = "344"
    name: str = "TradSesCloseTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
