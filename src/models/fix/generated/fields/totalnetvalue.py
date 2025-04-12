
from .base import FIXFieldBase
from .types import FIXAmt

class TotalNetValue(FIXFieldBase):
    """FIX TotalNetValue field."""
    tag: str = "900"
    name: str = "TotalNetValue"
    type: str = "AMT"
    value: FIXAmt
