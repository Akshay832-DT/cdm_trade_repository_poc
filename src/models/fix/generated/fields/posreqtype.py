
from .base import FIXFieldBase
from .types import FIXInt

class PosReqType(FIXFieldBase):
    """FIX PosReqType field."""
    tag: str = "724"
    name: str = "PosReqType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: POSITIONS
    # 1: TRADES
    # 2: EXERCISES
    # 3: ASSIGNMENTS
