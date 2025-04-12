
from .base import FIXFieldBase
from .types import FIXInt

class CrossType(FIXFieldBase):
    """FIX CrossType field."""
    tag: str = "549"
    name: str = "CrossType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: CROSS_AON
    # 2: CROSS_IOC
    # 3: CROSS_ONE_SIDE
    # 4: CROSS_SAME_PRICE
