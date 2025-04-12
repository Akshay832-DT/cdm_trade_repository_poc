
from .base import FIXFieldBase
from .types import FIXAmt

class UnderlyingStartValue(FIXFieldBase):
    """FIX UnderlyingStartValue field."""
    tag: str = "884"
    name: str = "UnderlyingStartValue"
    type: str = "AMT"
    value: FIXAmt
