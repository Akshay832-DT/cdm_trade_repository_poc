
from .base import FIXFieldBase
from .types import FIXFloat

class DiscretionOffsetValue(FIXFieldBase):
    """FIX DiscretionOffsetValue field."""
    tag: str = "389"
    name: str = "DiscretionOffsetValue"
    type: str = "FLOAT"
    value: FIXFloat
