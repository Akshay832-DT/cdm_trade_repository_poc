
from .base import FIXFieldBase
from .types import FIXString

class ClOrdID(FIXFieldBase):
    """FIX ClOrdID field."""
    tag: str = "11"
    name: str = "ClOrdID"
    type: str = "STRING"
    value: FIXString
