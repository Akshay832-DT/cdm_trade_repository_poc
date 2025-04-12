
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoMiscFees(FIXFieldBase):
    """FIX NoMiscFees field."""
    tag: str = "136"
    name: str = "NoMiscFees"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
