
from .base import FIXFieldBase
from .types import FIXString

class SettlInstMsgID(FIXFieldBase):
    """FIX SettlInstMsgID field."""
    tag: str = "777"
    name: str = "SettlInstMsgID"
    type: str = "STRING"
    value: FIXString
