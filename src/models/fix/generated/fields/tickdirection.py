
from .base import FIXFieldBase
from .types import FIXChar

class TickDirection(FIXFieldBase):
    """FIX TickDirection field."""
    tag: str = "274"
    name: str = "TickDirection"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: PLUS_TICK
    # 1: ZERO_PLUS_TICK
    # 2: MINUS_TICK
    # 3: ZERO_MINUS_TICK
