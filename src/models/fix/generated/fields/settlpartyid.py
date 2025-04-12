
from .base import FIXFieldBase
from .types import FIXString

class SettlPartyID(FIXFieldBase):
    """FIX SettlPartyID field."""
    tag: str = "782"
    name: str = "SettlPartyID"
    type: str = "STRING"
    value: FIXString
