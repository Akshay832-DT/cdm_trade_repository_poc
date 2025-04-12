
from .base import FIXFieldBase
from .types import FIXExchange

class MDMkt(FIXFieldBase):
    """FIX MDMkt field."""
    tag: str = "275"
    name: str = "MDMkt"
    type: str = "EXCHANGE"
    value: FIXExchange
