
from .base import FIXFieldBase
from .types import FIXString

class SettlSessSubID(FIXFieldBase):
    """FIX SettlSessSubID field."""
    tag: str = "717"
    name: str = "SettlSessSubID"
    type: str = "STRING"
    value: FIXString
