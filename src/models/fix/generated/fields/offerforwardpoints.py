
from .base import FIXFieldBase
from .types import FIXString

class OfferForwardPoints(FIXFieldBase):
    """FIX OfferForwardPoints field."""
    tag: str = "191"
    name: str = "OfferForwardPoints"
    type: str = "PRICEOFFSET"
    value: FIXString
