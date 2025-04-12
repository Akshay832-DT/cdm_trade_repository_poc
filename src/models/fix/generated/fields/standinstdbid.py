
from .base import FIXFieldBase
from .types import FIXString

class StandInstDbID(FIXFieldBase):
    """FIX StandInstDbID field."""
    tag: str = "171"
    name: str = "StandInstDbID"
    type: str = "STRING"
    value: FIXString
