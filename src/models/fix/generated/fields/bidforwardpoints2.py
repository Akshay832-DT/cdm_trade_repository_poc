
from .base import FIXFieldBase
from .types import FIXString

class BidForwardPoints2(FIXFieldBase):
    """FIX BidForwardPoints2 field."""
    tag: str = "642"
    name: str = "BidForwardPoints2"
    type: str = "PRICEOFFSET"
    value: FIXString
