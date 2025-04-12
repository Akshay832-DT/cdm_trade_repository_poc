
from .base import FIXFieldBase
from .types import FIXString

class SettlInstRefID(FIXFieldBase):
    """FIX SettlInstRefID field."""
    tag: str = "214"
    name: str = "SettlInstRefID"
    type: str = "STRING"
    value: FIXString
