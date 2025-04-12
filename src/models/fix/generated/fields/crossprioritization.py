
from .base import FIXFieldBase
from .types import FIXInt

class CrossPrioritization(FIXFieldBase):
    """FIX CrossPrioritization field."""
    tag: str = "550"
    name: str = "CrossPrioritization"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: NONE
    # 1: BUY_SIDE_IS_PRIORITIZED
    # 2: SELL_SIDE_IS_PRIORITIZED
