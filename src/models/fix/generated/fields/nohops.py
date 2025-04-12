
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoHops(FIXFieldBase):
    """FIX NoHops field."""
    tag: str = "627"
    name: str = "NoHops"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
