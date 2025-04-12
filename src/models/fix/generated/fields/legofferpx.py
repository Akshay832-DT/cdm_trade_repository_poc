
from .base import FIXFieldBase
from .types import FIXPrice

class LegOfferPx(FIXFieldBase):
    """FIX LegOfferPx field."""
    tag: str = "684"
    name: str = "LegOfferPx"
    type: str = "PRICE"
    value: FIXPrice
