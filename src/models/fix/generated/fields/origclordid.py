
from .base import FIXFieldBase
from .types import FIXString

class OrigClOrdID(FIXFieldBase):
    """FIX OrigClOrdID field."""
    tag: str = "41"
    name: str = "OrigClOrdID"
    type: str = "STRING"
    value: FIXString
