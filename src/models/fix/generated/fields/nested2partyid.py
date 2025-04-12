
from .base import FIXFieldBase
from .types import FIXString

class Nested2PartyID(FIXFieldBase):
    """FIX Nested2PartyID field."""
    tag: str = "757"
    name: str = "Nested2PartyID"
    type: str = "STRING"
    value: FIXString
