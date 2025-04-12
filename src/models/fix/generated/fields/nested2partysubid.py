
from .base import FIXFieldBase
from .types import FIXString

class Nested2PartySubID(FIXFieldBase):
    """FIX Nested2PartySubID field."""
    tag: str = "760"
    name: str = "Nested2PartySubID"
    type: str = "STRING"
    value: FIXString
