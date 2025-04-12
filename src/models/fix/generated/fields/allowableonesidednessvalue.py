
from .base import FIXFieldBase
from .types import FIXAmt

class AllowableOneSidednessValue(FIXFieldBase):
    """FIX AllowableOneSidednessValue field."""
    tag: str = "766"
    name: str = "AllowableOneSidednessValue"
    type: str = "AMT"
    value: FIXAmt
