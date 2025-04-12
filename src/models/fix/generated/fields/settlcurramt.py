
from .base import FIXFieldBase
from .types import FIXAmt

class SettlCurrAmt(FIXFieldBase):
    """FIX SettlCurrAmt field."""
    tag: str = "119"
    name: str = "SettlCurrAmt"
    type: str = "AMT"
    value: FIXAmt
