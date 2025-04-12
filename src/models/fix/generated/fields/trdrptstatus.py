
from .base import FIXFieldBase
from .types import FIXInt

class TrdRptStatus(FIXFieldBase):
    """FIX TrdRptStatus field."""
    tag: str = "939"
    name: str = "TrdRptStatus"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: ACCEPTED
    # 1: REJECTED
