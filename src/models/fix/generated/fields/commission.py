
from .base import FIXFieldBase
from .types import FIXAmt

class Commission(FIXFieldBase):
    """FIX Commission field."""
    tag: str = "12"
    name: str = "Commission"
    type: str = "AMT"
    value: FIXAmt
