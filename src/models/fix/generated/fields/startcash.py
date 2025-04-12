
from .base import FIXFieldBase
from .types import FIXAmt

class StartCash(FIXFieldBase):
    """FIX StartCash field."""
    tag: str = "921"
    name: str = "StartCash"
    type: str = "AMT"
    value: FIXAmt
