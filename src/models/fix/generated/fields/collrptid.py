
from .base import FIXFieldBase
from .types import FIXString

class CollRptID(FIXFieldBase):
    """FIX CollRptID field."""
    tag: str = "908"
    name: str = "CollRptID"
    type: str = "STRING"
    value: FIXString
