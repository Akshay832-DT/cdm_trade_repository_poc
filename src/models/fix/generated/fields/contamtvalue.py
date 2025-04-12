
from .base import FIXFieldBase
from .types import FIXFloat

class ContAmtValue(FIXFieldBase):
    """FIX ContAmtValue field."""
    tag: str = "520"
    name: str = "ContAmtValue"
    type: str = "FLOAT"
    value: FIXFloat
