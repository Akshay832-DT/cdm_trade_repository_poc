
from .base import FIXFieldBase
from .types import FIXString

class LegRefID(FIXFieldBase):
    """FIX LegRefID field."""
    tag: str = "654"
    name: str = "LegRefID"
    type: str = "STRING"
    value: FIXString
