
from .base import FIXFieldBase
from .types import FIXString

class CollAsgnID(FIXFieldBase):
    """FIX CollAsgnID field."""
    tag: str = "902"
    name: str = "CollAsgnID"
    type: str = "STRING"
    value: FIXString
