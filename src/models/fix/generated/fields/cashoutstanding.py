
from .base import FIXFieldBase
from .types import FIXAmt

class CashOutstanding(FIXFieldBase):
    """FIX CashOutstanding field."""
    tag: str = "901"
    name: str = "CashOutstanding"
    type: str = "AMT"
    value: FIXAmt
