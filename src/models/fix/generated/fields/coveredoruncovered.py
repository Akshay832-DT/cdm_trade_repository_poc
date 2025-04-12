
from .base import FIXFieldBase
from .types import FIXInt

class CoveredOrUncovered(FIXFieldBase):
    """FIX CoveredOrUncovered field."""
    tag: str = "203"
    name: str = "CoveredOrUncovered"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: COVERED
    # 1: UNCOVERED
