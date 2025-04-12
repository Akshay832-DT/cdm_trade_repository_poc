
from .base import FIXFieldBase
from .types import FIXString

class MDEntryBuyer(FIXFieldBase):
    """FIX MDEntryBuyer field."""
    tag: str = "288"
    name: str = "MDEntryBuyer"
    type: str = "STRING"
    value: FIXString
