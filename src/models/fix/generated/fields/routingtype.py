
from .base import FIXFieldBase
from .types import FIXInt

class RoutingType(FIXFieldBase):
    """FIX RoutingType field."""
    tag: str = "216"
    name: str = "RoutingType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: TARGET_FIRM
    # 2: TARGET_LIST
    # 3: BLOCK_FIRM
    # 4: BLOCK_LIST
