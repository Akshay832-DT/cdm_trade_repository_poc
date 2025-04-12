
from .base import FIXFieldBase
from .types import FIXAmt

class PosAmt(FIXFieldBase):
    """FIX PosAmt field."""
    tag: str = "708"
    name: str = "PosAmt"
    type: str = "AMT"
    value: FIXAmt
