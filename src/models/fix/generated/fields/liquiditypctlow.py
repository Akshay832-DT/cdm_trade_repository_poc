
from .base import FIXFieldBase
from .types import FIXPercentage

class LiquidityPctLow(FIXFieldBase):
    """FIX LiquidityPctLow field."""
    tag: str = "402"
    name: str = "LiquidityPctLow"
    type: str = "PERCENTAGE"
    value: FIXPercentage
