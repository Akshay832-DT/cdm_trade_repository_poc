
from .base import FIXFieldBase
from .types import FIXInt

class LiquidityIndType(FIXFieldBase):
    """FIX LiquidityIndType field."""
    tag: str = "409"
    name: str = "LiquidityIndType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: FIVE_DAY_MOVING_AVERAGE
    # 2: TWENTY_DAY_MOVING_AVERAGE
    # 3: NORMAL_MARKET_SIZE
    # 4: OTHER
