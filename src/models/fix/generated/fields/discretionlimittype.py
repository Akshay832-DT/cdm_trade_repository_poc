
from .base import FIXFieldBase
from .types import FIXInt

class DiscretionLimitType(FIXFieldBase):
    """FIX DiscretionLimitType field."""
    tag: str = "843"
    name: str = "DiscretionLimitType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: OR_BETTER
    # 1: STRICT
    # 2: OR_WORSE
