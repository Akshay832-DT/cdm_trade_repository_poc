
from .base import FIXFieldBase
from .types import FIXInt

class TradeAllocIndicator(FIXFieldBase):
    """FIX TradeAllocIndicator field."""
    tag: str = "826"
    name: str = "TradeAllocIndicator"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: ALLOCATION_NOT_REQUIRED
    # 1: ALLOCATION_REQUIRED
    # 2: USE_ALLOCATION_PROVIDED_WITH_THE_TRADE
