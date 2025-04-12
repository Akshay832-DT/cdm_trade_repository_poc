
from .base import FIXFieldBase
from .types import FIXInt

class PegLimitType(FIXFieldBase):
    """FIX PegLimitType field."""
    tag: str = "837"
    name: str = "PegLimitType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: OR_BETTER
    # 1: STRICT
    # 2: OR_WORSE
