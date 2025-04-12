
from .base import FIXFieldBase
from .types import FIXPrice

class MktOfferPx(FIXFieldBase):
    """FIX MktOfferPx field."""
    tag: str = "646"
    name: str = "MktOfferPx"
    type: str = "PRICE"
    value: FIXPrice
