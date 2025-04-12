
from .base import FIXFieldBase
from .types import FIXString

class SettlPartySubID(FIXFieldBase):
    """FIX SettlPartySubID field."""
    tag: str = "785"
    name: str = "SettlPartySubID"
    type: str = "STRING"
    value: FIXString
