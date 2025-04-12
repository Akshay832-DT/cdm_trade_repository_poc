
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoPartyIDs(FIXFieldBase):
    """FIX NoPartyIDs field."""
    tag: str = "453"
    name: str = "NoPartyIDs"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
