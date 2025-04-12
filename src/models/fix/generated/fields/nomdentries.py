
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoMDEntries(FIXFieldBase):
    """FIX NoMDEntries field."""
    tag: str = "268"
    name: str = "NoMDEntries"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
