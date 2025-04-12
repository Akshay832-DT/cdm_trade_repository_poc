
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoStipulations(FIXFieldBase):
    """FIX NoStipulations field."""
    tag: str = "232"
    name: str = "NoStipulations"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
