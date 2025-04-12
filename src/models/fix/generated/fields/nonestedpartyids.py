
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoNestedPartyIDs(FIXFieldBase):
    """FIX NoNestedPartyIDs field."""
    tag: str = "539"
    name: str = "NoNestedPartyIDs"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
