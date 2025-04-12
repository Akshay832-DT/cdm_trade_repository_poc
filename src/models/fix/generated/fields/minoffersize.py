
from .base import FIXFieldBase
from .types import FIXQty

class MinOfferSize(FIXFieldBase):
    """FIX MinOfferSize field."""
    tag: str = "648"
    name: str = "MinOfferSize"
    type: str = "QTY"
    value: FIXQty
