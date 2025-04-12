
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoPositions(FIXFieldBase):
    """FIX NoPositions field."""
    tag: str = "702"
    name: str = "NoPositions"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
