
from .base import FIXFieldBase
from .types import FIXString

class AllocText(FIXFieldBase):
    """FIX AllocText field."""
    tag: str = "161"
    name: str = "AllocText"
    type: str = "STRING"
    value: FIXString
