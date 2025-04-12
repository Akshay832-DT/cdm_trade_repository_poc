
from .base import FIXFieldBase
from .types import FIXInt

class PegOffsetType(FIXFieldBase):
    """FIX PegOffsetType field."""
    tag: str = "836"
    name: str = "PegOffsetType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: PRICE
    # 1: BASIS_POINTS
    # 2: TICKS
    # 3: PRICE_TIER
