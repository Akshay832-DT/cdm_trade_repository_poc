
from .base import FIXFieldBase
from .types import FIXAmt

class OpenInterest(FIXFieldBase):
    """FIX OpenInterest field."""
    tag: str = "746"
    name: str = "OpenInterest"
    type: str = "AMT"
    value: FIXAmt
