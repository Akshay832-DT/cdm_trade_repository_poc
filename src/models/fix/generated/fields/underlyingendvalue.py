
from .base import FIXFieldBase
from .types import FIXAmt

class UnderlyingEndValue(FIXFieldBase):
    """FIX UnderlyingEndValue field."""
    tag: str = "886"
    name: str = "UnderlyingEndValue"
    type: str = "AMT"
    value: FIXAmt
