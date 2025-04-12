
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingStipType(FIXFieldBase):
    """FIX UnderlyingStipType field."""
    tag: str = "888"
    name: str = "UnderlyingStipType"
    type: str = "STRING"
    value: FIXString
