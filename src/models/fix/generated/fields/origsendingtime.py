
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class OrigSendingTime(FIXFieldBase):
    """FIX OrigSendingTime field."""
    tag: str = "122"
    name: str = "OrigSendingTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
