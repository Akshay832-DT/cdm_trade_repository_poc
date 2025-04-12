
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoSettlPartyIDs(FIXFieldBase):
    """FIX NoSettlPartyIDs field."""
    tag: str = "781"
    name: str = "NoSettlPartyIDs"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
