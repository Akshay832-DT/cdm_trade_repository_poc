
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoEvents(FIXFieldBase):
    """FIX NoEvents field."""
    tag: str = "864"
    name: str = "NoEvents"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
