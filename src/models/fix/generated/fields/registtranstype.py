
from .base import FIXFieldBase
from .types import FIXChar

class RegistTransType(FIXFieldBase):
    """FIX RegistTransType field."""
    tag: str = "514"
    name: str = "RegistTransType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: NEW
    # 1: REPLACE
    # 2: CANCEL
