
from .base import FIXFieldBase
from .types import FIXQty

class MDEntrySize(FIXFieldBase):
    """FIX MDEntrySize field."""
    tag: str = "271"
    name: str = "MDEntrySize"
    type: str = "QTY"
    value: FIXQty
