
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoStrikes(FIXFieldBase):
    """FIX NoStrikes field."""
    tag: str = "428"
    name: str = "NoStrikes"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
