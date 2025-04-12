
from .base import FIXFieldBase
from .types import FIXString

class Nested3PartyID(FIXFieldBase):
    """FIX Nested3PartyID field."""
    tag: str = "949"
    name: str = "Nested3PartyID"
    type: str = "STRING"
    value: FIXString
