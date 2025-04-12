
from .base import FIXFieldBase
from .types import FIXString

class NestedPartyID(FIXFieldBase):
    """FIX NestedPartyID field."""
    tag: str = "524"
    name: str = "NestedPartyID"
    type: str = "STRING"
    value: FIXString
