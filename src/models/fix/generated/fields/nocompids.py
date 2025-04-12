
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoCompIDs(FIXFieldBase):
    """FIX NoCompIDs field."""
    tag: str = "936"
    name: str = "NoCompIDs"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
