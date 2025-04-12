
from .base import FIXFieldBase
from .types import FIXString

class NestedPartySubID(FIXFieldBase):
    """FIX NestedPartySubID field."""
    tag: str = "545"
    name: str = "NestedPartySubID"
    type: str = "STRING"
    value: FIXString
