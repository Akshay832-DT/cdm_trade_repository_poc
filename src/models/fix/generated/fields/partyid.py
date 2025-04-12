
from .base import FIXFieldBase
from .types import FIXString

class PartyID(FIXFieldBase):
    """FIX PartyID field."""
    tag: str = "448"
    name: str = "PartyID"
    type: str = "STRING"
    value: FIXString
