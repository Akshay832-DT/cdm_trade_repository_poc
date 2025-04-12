
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoDates(FIXFieldBase):
    """FIX NoDates field."""
    tag: str = "580"
    name: str = "NoDates"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
