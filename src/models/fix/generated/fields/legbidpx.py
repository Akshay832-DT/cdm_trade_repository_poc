
from .base import FIXFieldBase
from .types import FIXPrice

class LegBidPx(FIXFieldBase):
    """FIX LegBidPx field."""
    tag: str = "681"
    name: str = "LegBidPx"
    type: str = "PRICE"
    value: FIXPrice
