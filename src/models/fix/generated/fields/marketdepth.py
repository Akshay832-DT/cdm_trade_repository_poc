
from .base import FIXFieldBase
from .types import FIXInt

class MarketDepth(FIXFieldBase):
    """FIX MarketDepth field."""
    tag: str = "264"
    name: str = "MarketDepth"
    type: str = "INT"
    value: FIXInt
