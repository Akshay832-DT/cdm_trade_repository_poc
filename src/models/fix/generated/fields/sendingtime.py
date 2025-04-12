
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class SendingTime(FIXFieldBase):
    """FIX SendingTime field."""
    tag: str = "52"
    name: str = "SendingTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
