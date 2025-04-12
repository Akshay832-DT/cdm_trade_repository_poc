
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class StrikeTime(FIXFieldBase):
    """FIX StrikeTime field."""
    tag: str = "443"
    name: str = "StrikeTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
