
from .base import FIXFieldBase
from .types import FIXExchange

class LegSecurityExchange(FIXFieldBase):
    """FIX LegSecurityExchange field."""
    tag: str = "616"
    name: str = "LegSecurityExchange"
    type: str = "EXCHANGE"
    value: FIXExchange
