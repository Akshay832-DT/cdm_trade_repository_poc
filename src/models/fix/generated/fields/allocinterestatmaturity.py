
from .base import FIXFieldBase
from .types import FIXAmt

class AllocInterestAtMaturity(FIXFieldBase):
    """FIX AllocInterestAtMaturity field."""
    tag: str = "741"
    name: str = "AllocInterestAtMaturity"
    type: str = "AMT"
    value: FIXAmt
