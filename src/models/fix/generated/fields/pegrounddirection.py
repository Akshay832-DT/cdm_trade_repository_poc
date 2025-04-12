
from .base import FIXFieldBase
from .types import FIXInt

class PegRoundDirection(FIXFieldBase):
    """FIX PegRoundDirection field."""
    tag: str = "838"
    name: str = "PegRoundDirection"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: MORE_AGGRESSIVE
    # 2: MORE_PASSIVE
