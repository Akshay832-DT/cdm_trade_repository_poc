
from .base import FIXFieldBase
from .types import FIXFloat

class PegOffsetValue(FIXFieldBase):
    """FIX PegOffsetValue field."""
    tag: str = "211"
    name: str = "PegOffsetValue"
    type: str = "FLOAT"
    value: FIXFloat
