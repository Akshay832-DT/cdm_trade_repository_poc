
from .base import FIXFieldBase
from .types import FIXUTCTimestamp

class EffectiveTime(FIXFieldBase):
    """FIX EffectiveTime field."""
    tag: str = "168"
    name: str = "EffectiveTime"
    type: str = "UTCTIMESTAMP"
    value: FIXUTCTimestamp
