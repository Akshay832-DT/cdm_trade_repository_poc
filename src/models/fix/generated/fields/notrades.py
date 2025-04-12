
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoTrades(FIXFieldBase):
    """FIX NoTrades field."""
    tag: str = "897"
    name: str = "NoTrades"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
