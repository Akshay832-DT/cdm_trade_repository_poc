
from .base import FIXFieldBase
from .types import FIXPercentage

class BidYield(FIXFieldBase):
    """FIX BidYield field."""
    tag: str = "632"
    name: str = "BidYield"
    type: str = "PERCENTAGE"
    value: FIXPercentage
