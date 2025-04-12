
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class ExecValuationPoint(FIXFieldBase):
    """FIX ExecValuationPoint field."""
    tag: str = "515"
    name: str = "ExecValuationPoint"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
