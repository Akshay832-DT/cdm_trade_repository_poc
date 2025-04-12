
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoMDEntryTypes(FIXFieldBase):
    """FIX NoMDEntryTypes field."""
    tag: str = "267"
    name: str = "NoMDEntryTypes"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
