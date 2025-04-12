
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoNested3PartyIDs(FIXFieldBase):
    """FIX NoNested3PartyIDs field."""
    tag: str = "948"
    name: str = "NoNested3PartyIDs"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
