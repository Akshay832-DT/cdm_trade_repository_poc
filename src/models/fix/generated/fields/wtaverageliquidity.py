
from .base import FIXFieldBase
from .types import FIXPercentage

class WtAverageLiquidity(FIXFieldBase):
    """FIX WtAverageLiquidity field."""
    tag: str = "410"
    name: str = "WtAverageLiquidity"
    type: str = "PERCENTAGE"
    value: FIXPercentage
