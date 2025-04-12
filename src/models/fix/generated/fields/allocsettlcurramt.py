
from .base import FIXFieldBase
from .types import FIXAmt

class AllocSettlCurrAmt(FIXFieldBase):
    """FIX AllocSettlCurrAmt field."""
    tag: str = "737"
    name: str = "AllocSettlCurrAmt"
    type: str = "AMT"
    value: FIXAmt
