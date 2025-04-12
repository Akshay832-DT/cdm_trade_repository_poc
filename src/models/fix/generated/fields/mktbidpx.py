
from .base import FIXFieldBase
from .types import FIXPrice

class MktBidPx(FIXFieldBase):
    """FIX MktBidPx field."""
    tag: str = "645"
    name: str = "MktBidPx"
    type: str = "PRICE"
    value: FIXPrice
