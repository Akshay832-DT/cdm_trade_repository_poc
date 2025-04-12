
from .base import FIXFieldBase
from .types import FIXInt

class AvgPxIndicator(FIXFieldBase):
    """FIX AvgPxIndicator field."""
    tag: str = "819"
    name: str = "AvgPxIndicator"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: NO_AVERAGE_PRICING
    # 1: TRADE
    # 2: LAST_TRADE
