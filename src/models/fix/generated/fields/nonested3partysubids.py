
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoNested3PartySubIDs(FIXFieldBase):
    """FIX NoNested3PartySubIDs field."""
    tag: str = "952"
    name: str = "NoNested3PartySubIDs"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
