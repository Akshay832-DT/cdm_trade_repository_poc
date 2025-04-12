
from .base import FIXFieldBase
from .types import FIXString

class TrdMatchID(FIXFieldBase):
    """FIX TrdMatchID field."""
    tag: str = "880"
    name: str = "TrdMatchID"
    type: str = "STRING"
    value: FIXString
