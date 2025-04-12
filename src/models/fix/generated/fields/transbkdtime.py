
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class TransBkdTime(FIXFieldBase):
    """FIX TransBkdTime field."""
    tag: str = "483"
    name: str = "TransBkdTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
