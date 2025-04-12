
from .base import FIXFieldBase
from .types import FIXInt

class PegMoveType(FIXFieldBase):
    """FIX PegMoveType field."""
    tag: str = "835"
    name: str = "PegMoveType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: FLOATING
    # 1: FIXED
