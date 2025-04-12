
from .base import FIXFieldBase
from .types import FIXString

class Nested3PartySubID(FIXFieldBase):
    """FIX Nested3PartySubID field."""
    tag: str = "953"
    name: str = "Nested3PartySubID"
    type: str = "STRING"
    value: FIXString
