
from .base import FIXFieldBase
from .types import FIXString

class CollRespID(FIXFieldBase):
    """FIX CollRespID field."""
    tag: str = "904"
    name: str = "CollRespID"
    type: str = "STRING"
    value: FIXString
