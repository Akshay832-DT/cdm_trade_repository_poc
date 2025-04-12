
from .base import FIXFieldBase
from .types import FIXPrice

class OfferPx(FIXFieldBase):
    """FIX OfferPx field."""
    tag: str = "133"
    name: str = "OfferPx"
    type: str = "PRICE"
    value: FIXPrice
