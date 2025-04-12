
from .base import FIXFieldBase
from .types import FIXChar

class AllocTransType(FIXFieldBase):
    """FIX AllocTransType field."""
    tag: str = "71"
    name: str = "AllocTransType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: NEW
    # 1: REPLACE
    # 2: CANCEL
