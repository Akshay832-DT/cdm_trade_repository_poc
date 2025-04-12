
from .base import FIXFieldBase
from .types import FIXChar

class RoundingDirection(FIXFieldBase):
    """FIX RoundingDirection field."""
    tag: str = "468"
    name: str = "RoundingDirection"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: ROUND_TO_NEAREST
    # 1: ROUND_DOWN
    # 2: ROUND_UP
