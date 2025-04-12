
from .base import FIXFieldBase
from .types import FIXPrice

class OfferSpotRate(FIXFieldBase):
    """FIX OfferSpotRate field."""
    tag: str = "190"
    name: str = "OfferSpotRate"
    type: str = "PRICE"
    value: FIXPrice
