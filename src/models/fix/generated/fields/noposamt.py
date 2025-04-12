
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoPosAmt(FIXFieldBase):
    """FIX NoPosAmt field."""
    tag: str = "753"
    name: str = "NoPosAmt"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
