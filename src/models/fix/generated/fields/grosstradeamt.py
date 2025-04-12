
from .base import FIXFieldBase
from .types import FIXAmt

class GrossTradeAmt(FIXFieldBase):
    """FIX GrossTradeAmt field."""
    tag: str = "381"
    name: str = "GrossTradeAmt"
    type: str = "AMT"
    value: FIXAmt
