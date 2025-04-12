
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoCapacities(FIXFieldBase):
    """FIX NoCapacities field."""
    tag: str = "862"
    name: str = "NoCapacities"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
