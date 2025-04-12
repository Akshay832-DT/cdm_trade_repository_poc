
from .base import FIXFieldBase
from .types import FIXAmt

class TotalTakedown(FIXFieldBase):
    """FIX TotalTakedown field."""
    tag: str = "237"
    name: str = "TotalTakedown"
    type: str = "AMT"
    value: FIXAmt
