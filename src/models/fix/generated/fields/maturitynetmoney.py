
from .base import FIXFieldBase
from .types import FIXAmt

class MaturityNetMoney(FIXFieldBase):
    """FIX MaturityNetMoney field."""
    tag: str = "890"
    name: str = "MaturityNetMoney"
    type: str = "AMT"
    value: FIXAmt
