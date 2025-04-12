
from .base import FIXFieldBase
from .types import FIXLength

class MaxMessageSize(FIXFieldBase):
    """FIX MaxMessageSize field."""
    tag: str = "383"
    name: str = "MaxMessageSize"
    type: str = "LENGTH"
    value: FIXLength
