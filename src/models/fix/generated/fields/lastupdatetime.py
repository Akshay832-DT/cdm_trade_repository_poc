
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class LastUpdateTime(FIXFieldBase):
    """FIX LastUpdateTime field."""
    tag: str = "779"
    name: str = "LastUpdateTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
