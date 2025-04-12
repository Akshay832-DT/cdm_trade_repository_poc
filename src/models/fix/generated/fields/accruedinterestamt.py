
from .base import FIXFieldBase
from .types import FIXAmt

class AccruedInterestAmt(FIXFieldBase):
    """FIX AccruedInterestAmt field."""
    tag: str = "159"
    name: str = "AccruedInterestAmt"
    type: str = "AMT"
    value: FIXAmt
