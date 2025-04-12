
from .base import FIXFieldBase
from .types import FIXString

class MDEntryRefID(FIXFieldBase):
    """FIX MDEntryRefID field."""
    tag: str = "280"
    name: str = "MDEntryRefID"
    type: str = "STRING"
    value: FIXString
