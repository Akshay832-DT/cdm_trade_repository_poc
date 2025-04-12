
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoContAmts(FIXFieldBase):
    """FIX NoContAmts field."""
    tag: str = "518"
    name: str = "NoContAmts"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
