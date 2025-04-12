
from .base import FIXFieldBase
from .types import FIXAmt

class LiquidityValue(FIXFieldBase):
    """FIX LiquidityValue field."""
    tag: str = "404"
    name: str = "LiquidityValue"
    type: str = "AMT"
    value: FIXAmt
