
from .base import FIXFieldBase
from .types import FIXAmt

class SideValue1(FIXFieldBase):
    """FIX SideValue1 field."""
    tag: str = "396"
    name: str = "SideValue1"
    type: str = "AMT"
    value: FIXAmt
