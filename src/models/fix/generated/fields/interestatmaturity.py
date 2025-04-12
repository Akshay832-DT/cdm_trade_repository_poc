
from .base import FIXFieldBase
from .types import FIXAmt

class InterestAtMaturity(FIXFieldBase):
    """FIX InterestAtMaturity field."""
    tag: str = "738"
    name: str = "InterestAtMaturity"
    type: str = "AMT"
    value: FIXAmt
