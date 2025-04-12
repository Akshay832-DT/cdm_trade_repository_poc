
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoAffectedOrders(FIXFieldBase):
    """FIX NoAffectedOrders field."""
    tag: str = "534"
    name: str = "NoAffectedOrders"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
