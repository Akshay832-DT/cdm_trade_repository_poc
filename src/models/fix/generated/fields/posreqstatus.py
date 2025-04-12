
from .base import FIXFieldBase
from .types import FIXInt

class PosReqStatus(FIXFieldBase):
    """FIX PosReqStatus field."""
    tag: str = "729"
    name: str = "PosReqStatus"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: COMPLETED
    # 1: COMPLETED_WITH_WARNINGS
    # 2: REJECTED
