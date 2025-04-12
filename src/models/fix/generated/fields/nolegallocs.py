
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoLegAllocs(FIXFieldBase):
    """FIX NoLegAllocs field."""
    tag: str = "670"
    name: str = "NoLegAllocs"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
