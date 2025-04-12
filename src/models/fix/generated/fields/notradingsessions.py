
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoTradingSessions(FIXFieldBase):
    """FIX NoTradingSessions field."""
    tag: str = "386"
    name: str = "NoTradingSessions"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
