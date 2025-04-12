
from .base import FIXFieldBase
from .types import FIXExchange

class UnderlyingSecurityExchange(FIXFieldBase):
    """FIX UnderlyingSecurityExchange field."""
    tag: str = "308"
    name: str = "UnderlyingSecurityExchange"
    type: str = "EXCHANGE"
    value: FIXExchange
