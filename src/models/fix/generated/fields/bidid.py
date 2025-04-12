
from .base import FIXFieldBase
from .types import FIXString

class BidID(FIXFieldBase):
    """FIX BidID field."""
    tag: str = "390"
    name: str = "BidID"
    type: str = "STRING"
    value: FIXString
