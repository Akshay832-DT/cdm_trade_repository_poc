
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoDlvyInst(FIXFieldBase):
    """FIX NoDlvyInst field."""
    tag: str = "85"
    name: str = "NoDlvyInst"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
