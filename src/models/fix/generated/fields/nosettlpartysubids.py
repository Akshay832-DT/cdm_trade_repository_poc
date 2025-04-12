
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoSettlPartySubIDs(FIXFieldBase):
    """FIX NoSettlPartySubIDs field."""
    tag: str = "801"
    name: str = "NoSettlPartySubIDs"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
