
from .base import FIXFieldBase
from .types import FIXUTCTimeOnly

class MDEntryTime(FIXFieldBase):
    """FIX MDEntryTime field."""
    tag: str = "273"
    name: str = "MDEntryTime"
    type: str = "UTCTIMEONLY"
    value: FIXUTCTimeOnly
