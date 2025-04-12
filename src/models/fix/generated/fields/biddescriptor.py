
from .base import FIXFieldBase
from .types import FIXString

class BidDescriptor(FIXFieldBase):
    """FIX BidDescriptor field."""
    tag: str = "400"
    name: str = "BidDescriptor"
    type: str = "STRING"
    value: FIXString
