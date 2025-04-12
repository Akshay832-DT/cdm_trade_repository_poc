
from .base import FIXFieldBase
from .types import FIXQty

class OfferSize(FIXFieldBase):
    """FIX OfferSize field."""
    tag: str = "135"
    name: str = "OfferSize"
    type: str = "QTY"
    value: FIXQty
