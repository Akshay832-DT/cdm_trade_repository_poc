
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoNested2PartyIDs(FIXFieldBase):
    """FIX NoNested2PartyIDs field."""
    tag: str = "756"
    name: str = "NoNested2PartyIDs"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
