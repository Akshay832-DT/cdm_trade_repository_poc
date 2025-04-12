
from .base import FIXFieldBase
from .types import FIXAmt

class MarginExcess(FIXFieldBase):
    """FIX MarginExcess field."""
    tag: str = "899"
    name: str = "MarginExcess"
    type: str = "AMT"
    value: FIXAmt
