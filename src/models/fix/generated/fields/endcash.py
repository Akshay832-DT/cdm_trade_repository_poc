
from .base import FIXFieldBase
from .types import FIXAmt

class EndCash(FIXFieldBase):
    """FIX EndCash field."""
    tag: str = "922"
    name: str = "EndCash"
    type: str = "AMT"
    value: FIXAmt
