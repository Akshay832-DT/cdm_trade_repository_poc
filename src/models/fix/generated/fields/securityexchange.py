
from .base import FIXFieldBase
from .types import FIXExchange

class SecurityExchange(FIXFieldBase):
    """FIX SecurityExchange field."""
    tag: str = "207"
    name: str = "SecurityExchange"
    type: str = "EXCHANGE"
    value: FIXExchange
