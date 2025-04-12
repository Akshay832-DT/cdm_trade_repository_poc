
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoLegStipulations(FIXFieldBase):
    """FIX NoLegStipulations field."""
    tag: str = "683"
    name: str = "NoLegStipulations"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
