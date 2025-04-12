
from .base import FIXFieldBase
from .types import FIXAmt

class FairValue(FIXFieldBase):
    """FIX FairValue field."""
    tag: str = "406"
    name: str = "FairValue"
    type: str = "AMT"
    value: FIXAmt
