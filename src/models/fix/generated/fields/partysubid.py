
from .base import FIXFieldBase
from .types import FIXString

class PartySubID(FIXFieldBase):
    """FIX PartySubID field."""
    tag: str = "523"
    name: str = "PartySubID"
    type: str = "STRING"
    value: FIXString
