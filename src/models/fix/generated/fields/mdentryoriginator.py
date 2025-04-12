
from .base import FIXFieldBase
from .types import FIXString

class MDEntryOriginator(FIXFieldBase):
    """FIX MDEntryOriginator field."""
    tag: str = "282"
    name: str = "MDEntryOriginator"
    type: str = "STRING"
    value: FIXString
