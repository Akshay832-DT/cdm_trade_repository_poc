
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoLegs(FIXFieldBase):
    """FIX NoLegs field."""
    tag: str = "555"
    name: str = "NoLegs"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
