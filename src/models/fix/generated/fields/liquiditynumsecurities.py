
from .base import FIXFieldBase
from .types import FIXInt

class LiquidityNumSecurities(FIXFieldBase):
    """FIX LiquidityNumSecurities field."""
    tag: str = "441"
    name: str = "LiquidityNumSecurities"
    type: str = "INT"
    value: FIXInt
