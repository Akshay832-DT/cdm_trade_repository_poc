
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class TrdRegTimestamp(FIXFieldBase):
    """FIX TrdRegTimestamp field."""
    tag: str = "769"
    name: str = "TrdRegTimestamp"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
