
from .base import FIXFieldBase
from .types import FIXAmt

class AllocAccruedInterestAmt(FIXFieldBase):
    """FIX AllocAccruedInterestAmt field."""
    tag: str = "742"
    name: str = "AllocAccruedInterestAmt"
    type: str = "AMT"
    value: FIXAmt
