
from .base import FIXFieldBase
from .types import FIXAmt

class ValueOfFutures(FIXFieldBase):
    """FIX ValueOfFutures field."""
    tag: str = "408"
    name: str = "ValueOfFutures"
    type: str = "AMT"
    value: FIXAmt
