
from .base import FIXFieldBase
from .types import FIXChar

class AdvSide(FIXFieldBase):
    """FIX AdvSide field."""
    tag: str = "4"
    name: str = "AdvSide"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # B: BUY
    # S: SELL
    # X: CROSS
    # T: TRADE
