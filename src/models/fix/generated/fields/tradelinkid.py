
from .base import FIXFieldBase
from .types import FIXString

class TradeLinkID(FIXFieldBase):
    """FIX TradeLinkID field."""
    tag: str = "820"
    name: str = "TradeLinkID"
    type: str = "STRING"
    value: FIXString
