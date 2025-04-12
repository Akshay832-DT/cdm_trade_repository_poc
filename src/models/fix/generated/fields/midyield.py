
from .base import FIXFieldBase
from .types import FIXPercentage

class MidYield(FIXFieldBase):
    """FIX MidYield field."""
    tag: str = "633"
    name: str = "MidYield"
    type: str = "PERCENTAGE"
    value: FIXPercentage
