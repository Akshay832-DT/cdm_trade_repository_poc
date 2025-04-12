
from .base import FIXFieldBase
from .types import FIXString

class BidForwardPoints(FIXFieldBase):
    """FIX BidForwardPoints field."""
    tag: str = "189"
    name: str = "BidForwardPoints"
    type: str = "PRICEOFFSET"
    value: FIXString
