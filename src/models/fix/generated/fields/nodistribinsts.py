
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoDistribInsts(FIXFieldBase):
    """FIX NoDistribInsts field."""
    tag: str = "510"
    name: str = "NoDistribInsts"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
