
from .base import FIXFieldBase
from .types import FIXAmt

class AllocNetMoney(FIXFieldBase):
    """FIX AllocNetMoney field."""
    tag: str = "154"
    name: str = "AllocNetMoney"
    type: str = "AMT"
    value: FIXAmt
