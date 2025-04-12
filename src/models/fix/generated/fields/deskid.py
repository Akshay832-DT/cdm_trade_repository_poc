
from .base import FIXFieldBase
from .types import FIXString

class DeskID(FIXFieldBase):
    """FIX DeskID field."""
    tag: str = "284"
    name: str = "DeskID"
    type: str = "STRING"
    value: FIXString
