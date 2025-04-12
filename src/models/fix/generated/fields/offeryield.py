
from .base import FIXFieldBase
from .types import FIXPercentage

class OfferYield(FIXFieldBase):
    """FIX OfferYield field."""
    tag: str = "634"
    name: str = "OfferYield"
    type: str = "PERCENTAGE"
    value: FIXPercentage
