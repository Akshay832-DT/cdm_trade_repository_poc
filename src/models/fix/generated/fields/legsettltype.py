
from .base import FIXFieldBase
from .types import FIXChar

class LegSettlType(FIXFieldBase):
    """FIX LegSettlType field."""
    tag: str = "587"
    name: str = "LegSettlType"
    type: str = "CHAR"
    value: FIXChar
