
from .base import FIXFieldBase
from .types import FIXExchange

class LastMkt(FIXFieldBase):
    """FIX LastMkt field."""
    tag: str = "30"
    name: str = "LastMkt"
    type: str = "EXCHANGE"
    value: FIXExchange
