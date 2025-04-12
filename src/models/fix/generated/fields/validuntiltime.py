
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class ValidUntilTime(FIXFieldBase):
    """FIX ValidUntilTime field."""
    tag: str = "62"
    name: str = "ValidUntilTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
