
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoUnderlyingStips(FIXFieldBase):
    """FIX NoUnderlyingStips field."""
    tag: str = "887"
    name: str = "NoUnderlyingStips"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
