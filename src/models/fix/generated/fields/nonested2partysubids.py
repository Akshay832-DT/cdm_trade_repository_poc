
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoNested2PartySubIDs(FIXFieldBase):
    """FIX NoNested2PartySubIDs field."""
    tag: str = "806"
    name: str = "NoNested2PartySubIDs"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
