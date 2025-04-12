
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingStipValue(FIXFieldBase):
    """FIX UnderlyingStipValue field."""
    tag: str = "889"
    name: str = "UnderlyingStipValue"
    type: str = "STRING"
    value: FIXString
