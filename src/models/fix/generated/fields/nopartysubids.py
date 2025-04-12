
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoPartySubIDs(FIXFieldBase):
    """FIX NoPartySubIDs field."""
    tag: str = "802"
    name: str = "NoPartySubIDs"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
