
from .base import FIXFieldBase
from .types import FIXPercentage

class LiquidityPctHigh(FIXFieldBase):
    """FIX LiquidityPctHigh field."""
    tag: str = "403"
    name: str = "LiquidityPctHigh"
    type: str = "PERCENTAGE"
    value: FIXPercentage
