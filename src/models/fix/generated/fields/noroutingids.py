
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoRoutingIDs(FIXFieldBase):
    """FIX NoRoutingIDs field."""
    tag: str = "215"
    name: str = "NoRoutingIDs"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
