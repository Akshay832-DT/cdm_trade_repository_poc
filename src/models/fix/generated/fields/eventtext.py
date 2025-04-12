
from .base import FIXFieldBase
from .types import FIXString

class EventText(FIXFieldBase):
    """FIX EventText field."""
    tag: str = "868"
    name: str = "EventText"
    type: str = "STRING"
    value: FIXString
