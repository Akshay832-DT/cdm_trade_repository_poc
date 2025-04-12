
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class TransactTime(FIXFieldBase):
    """FIX TransactTime field."""
    tag: str = "60"
    name: str = "TransactTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
