
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoSettlInst(FIXFieldBase):
    """FIX NoSettlInst field."""
    tag: str = "778"
    name: str = "NoSettlInst"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
