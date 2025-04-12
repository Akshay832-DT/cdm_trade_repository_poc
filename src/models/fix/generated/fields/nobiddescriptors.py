
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoBidDescriptors(FIXFieldBase):
    """FIX NoBidDescriptors field."""
    tag: str = "398"
    name: str = "NoBidDescriptors"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
