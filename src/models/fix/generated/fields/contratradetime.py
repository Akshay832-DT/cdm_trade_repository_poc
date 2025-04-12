
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class ContraTradeTime(FIXFieldBase):
    """FIX ContraTradeTime field."""
    tag: str = "438"
    name: str = "ContraTradeTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
