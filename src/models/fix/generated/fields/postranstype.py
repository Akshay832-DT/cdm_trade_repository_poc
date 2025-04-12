
from .base import FIXFieldBase
from .types import FIXInt

class PosTransType(FIXFieldBase):
    """FIX PosTransType field."""
    tag: str = "709"
    name: str = "PosTransType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: EXERCISE
    # 2: DO_NOT_EXERCISE
    # 3: POSITION_ADJUSTMENT
    # 4: POSITION_CHANGE_SUBMISSION
    # 5: PLEDGE
