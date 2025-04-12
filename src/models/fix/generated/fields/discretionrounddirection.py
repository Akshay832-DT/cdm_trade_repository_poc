
from .base import FIXFieldBase
from .types import FIXInt

class DiscretionRoundDirection(FIXFieldBase):
    """FIX DiscretionRoundDirection field."""
    tag: str = "844"
    name: str = "DiscretionRoundDirection"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: MORE_AGGRESSIVE
    # 2: MORE_PASSIVE
