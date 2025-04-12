
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class TradSesStartTime(FIXFieldBase):
    """FIX TradSesStartTime field."""
    tag: str = "341"
    name: str = "TradSesStartTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
