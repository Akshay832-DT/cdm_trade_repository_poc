
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoRelatedSym(FIXFieldBase):
    """FIX NoRelatedSym field."""
    tag: str = "146"
    name: str = "NoRelatedSym"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
