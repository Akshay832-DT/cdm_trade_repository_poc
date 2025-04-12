
from .base import FIXFieldBase
from .types import FIXAmt

class UnderlyingCurrentValue(FIXFieldBase):
    """FIX UnderlyingCurrentValue field."""
    tag: str = "885"
    name: str = "UnderlyingCurrentValue"
    type: str = "AMT"
    value: FIXAmt
