
from .base import FIXFieldBase
from .types import FIXAmt

class TotalAccruedInterestAmt(FIXFieldBase):
    """FIX TotalAccruedInterestAmt field."""
    tag: str = "540"
    name: str = "TotalAccruedInterestAmt"
    type: str = "AMT"
    value: FIXAmt
