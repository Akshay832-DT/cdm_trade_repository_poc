
from .base import FIXFieldBase
from .types import FIXString

class SettlInstReqID(FIXFieldBase):
    """FIX SettlInstReqID field."""
    tag: str = "791"
    name: str = "SettlInstReqID"
    type: str = "STRING"
    value: FIXString
