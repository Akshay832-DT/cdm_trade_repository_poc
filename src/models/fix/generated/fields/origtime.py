
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class OrigTime(FIXFieldBase):
    """FIX OrigTime field."""
    tag: str = "42"
    name: str = "OrigTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
