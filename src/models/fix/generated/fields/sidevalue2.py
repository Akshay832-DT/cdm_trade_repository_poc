
from .base import FIXFieldBase
from .types import FIXAmt

class SideValue2(FIXFieldBase):
    """FIX SideValue2 field."""
    tag: str = "397"
    name: str = "SideValue2"
    type: str = "AMT"
    value: FIXAmt
