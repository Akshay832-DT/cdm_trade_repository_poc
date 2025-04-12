
from .base import FIXFieldBase
from .types import FIXQty

class DefOfferSize(FIXFieldBase):
    """FIX DefOfferSize field."""
    tag: str = "294"
    name: str = "DefOfferSize"
    type: str = "QTY"
    value: FIXQty
