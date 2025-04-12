
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class OrigOrdModTime(FIXFieldBase):
    """FIX OrigOrdModTime field."""
    tag: str = "586"
    name: str = "OrigOrdModTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
