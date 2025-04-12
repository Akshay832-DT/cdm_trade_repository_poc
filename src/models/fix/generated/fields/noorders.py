
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoOrders(FIXFieldBase):
    """FIX NoOrders field."""
    tag: str = "73"
    name: str = "NoOrders"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
