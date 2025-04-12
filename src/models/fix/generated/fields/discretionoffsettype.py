
from .base import FIXFieldBase
from .types import FIXInt

class DiscretionOffsetType(FIXFieldBase):
    """FIX DiscretionOffsetType field."""
    tag: str = "842"
    name: str = "DiscretionOffsetType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: PRICE
    # 1: BASIS_POINTS
    # 2: TICKS
    # 3: PRICE_TIER
