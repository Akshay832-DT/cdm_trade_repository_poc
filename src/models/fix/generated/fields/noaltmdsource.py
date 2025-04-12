
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoAltMDSource(FIXFieldBase):
    """FIX NoAltMDSource field."""
    tag: str = "816"
    name: str = "NoAltMDSource"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
