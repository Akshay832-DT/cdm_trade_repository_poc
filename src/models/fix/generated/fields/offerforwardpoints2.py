
from .base import FIXFieldBase
from .types import FIXString

class OfferForwardPoints2(FIXFieldBase):
    """FIX OfferForwardPoints2 field."""
    tag: str = "643"
    name: str = "OfferForwardPoints2"
    type: str = "PRICEOFFSET"
    value: FIXString
