
from .base import FIXFieldBase
from .types import FIXAmt

class MiscFeeAmt(FIXFieldBase):
    """FIX MiscFeeAmt field."""
    tag: str = "137"
    name: str = "MiscFeeAmt"
    type: str = "AMT"
    value: FIXAmt
