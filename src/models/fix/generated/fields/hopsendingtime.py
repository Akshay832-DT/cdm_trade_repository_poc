
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class HopSendingTime(FIXFieldBase):
    """FIX HopSendingTime field."""
    tag: str = "629"
    name: str = "HopSendingTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
