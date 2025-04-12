
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoTrdRegTimestamps(FIXFieldBase):
    """FIX NoTrdRegTimestamps field."""
    tag: str = "768"
    name: str = "NoTrdRegTimestamps"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
