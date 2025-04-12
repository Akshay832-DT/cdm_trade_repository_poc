
from .base import FIXFieldBase
from .types import FIXString

class LegPool(FIXFieldBase):
    """FIX LegPool field."""
    tag: str = "740"
    name: str = "LegPool"
    type: str = "STRING"
    value: FIXString
