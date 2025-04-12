
from .base import FIXFieldBase
from .types import FIXInt

class AllocAcctIDSource(FIXFieldBase):
    """FIX AllocAcctIDSource field."""
    tag: str = "661"
    name: str = "AllocAcctIDSource"
    type: str = "INT"
    value: FIXInt
