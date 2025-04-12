
from .base import FIXFieldBase
from .types import FIXString

class CollReqID(FIXFieldBase):
    """FIX CollReqID field."""
    tag: str = "894"
    name: str = "CollReqID"
    type: str = "STRING"
    value: FIXString
