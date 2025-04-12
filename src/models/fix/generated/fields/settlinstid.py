
from .base import FIXFieldBase
from .types import FIXString

class SettlInstID(FIXFieldBase):
    """FIX SettlInstID field."""
    tag: str = "162"
    name: str = "SettlInstID"
    type: str = "STRING"
    value: FIXString
