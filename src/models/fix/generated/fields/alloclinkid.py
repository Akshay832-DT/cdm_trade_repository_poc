
from .base import FIXFieldBase
from .types import FIXString

class AllocLinkID(FIXFieldBase):
    """FIX AllocLinkID field."""
    tag: str = "196"
    name: str = "AllocLinkID"
    type: str = "STRING"
    value: FIXString
