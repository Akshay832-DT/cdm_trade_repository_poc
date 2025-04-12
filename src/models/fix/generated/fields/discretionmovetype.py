
from .base import FIXFieldBase
from .types import FIXInt

class DiscretionMoveType(FIXFieldBase):
    """FIX DiscretionMoveType field."""
    tag: str = "841"
    name: str = "DiscretionMoveType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: FLOATING
    # 1: FIXED
