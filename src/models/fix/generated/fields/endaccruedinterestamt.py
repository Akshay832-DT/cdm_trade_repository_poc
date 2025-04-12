
from .base import FIXFieldBase
from .types import FIXAmt

class EndAccruedInterestAmt(FIXFieldBase):
    """FIX EndAccruedInterestAmt field."""
    tag: str = "920"
    name: str = "EndAccruedInterestAmt"
    type: str = "AMT"
    value: FIXAmt
