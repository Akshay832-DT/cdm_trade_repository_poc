
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoNestedPartySubIDs(FIXFieldBase):
    """FIX NoNestedPartySubIDs field."""
    tag: str = "804"
    name: str = "NoNestedPartySubIDs"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
