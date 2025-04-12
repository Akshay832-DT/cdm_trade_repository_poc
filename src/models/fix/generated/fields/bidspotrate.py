
from .base import FIXFieldBase
from .types import FIXPrice

class BidSpotRate(FIXFieldBase):
    """FIX BidSpotRate field."""
    tag: str = "188"
    name: str = "BidSpotRate"
    type: str = "PRICE"
    value: FIXPrice
