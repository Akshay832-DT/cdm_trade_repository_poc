
from .base import FIXFieldBase
from .types import FIXPercentage

class Yield(FIXFieldBase):
    """FIX Yield field."""
    tag: str = "236"
    name: str = "Yield"
    type: str = "PERCENTAGE"
    value: FIXPercentage
