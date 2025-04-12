
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoBidComponents(FIXFieldBase):
    """FIX NoBidComponents field."""
    tag: str = "420"
    name: str = "NoBidComponents"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
