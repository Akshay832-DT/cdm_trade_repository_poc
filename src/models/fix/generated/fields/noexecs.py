
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoExecs(FIXFieldBase):
    """FIX NoExecs field."""
    tag: str = "124"
    name: str = "NoExecs"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
