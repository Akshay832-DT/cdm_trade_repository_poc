
from .base import FIXFieldBase
from .types import FIXString

class ListID(FIXFieldBase):
    """FIX ListID field."""
    tag: str = "66"
    name: str = "ListID"
    type: str = "STRING"
    value: FIXString
