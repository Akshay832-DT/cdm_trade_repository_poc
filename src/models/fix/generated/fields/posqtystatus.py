
from .base import FIXFieldBase
from .types import FIXInt

class PosQtyStatus(FIXFieldBase):
    """FIX PosQtyStatus field."""
    tag: str = "706"
    name: str = "PosQtyStatus"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: SUBMITTED
    # 1: ACCEPTED
    # 2: REJECTED
