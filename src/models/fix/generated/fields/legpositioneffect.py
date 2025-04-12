
from .base import FIXFieldBase
from .types import FIXChar

class LegPositionEffect(FIXFieldBase):
    """FIX LegPositionEffect field."""
    tag: str = "564"
    name: str = "LegPositionEffect"
    type: str = "CHAR"
    value: FIXChar
