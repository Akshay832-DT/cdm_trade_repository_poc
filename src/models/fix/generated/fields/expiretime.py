
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class ExpireTime(FIXFieldBase):
    """FIX ExpireTime field."""
    tag: str = "126"
    name: str = "ExpireTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
