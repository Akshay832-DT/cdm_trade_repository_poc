
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoUnderlyings(FIXFieldBase):
    """FIX NoUnderlyings field."""
    tag: str = "711"
    name: str = "NoUnderlyings"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
