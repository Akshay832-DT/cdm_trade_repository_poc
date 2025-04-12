
from .base import FIXFieldBase
from .types import FIXAmt

class SharedCommission(FIXFieldBase):
    """FIX SharedCommission field."""
    tag: str = "858"
    name: str = "SharedCommission"
    type: str = "AMT"
    value: FIXAmt
