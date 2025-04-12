
from .base import FIXFieldBase
from .types import FIXExchange

class ExDestination(FIXFieldBase):
    """FIX ExDestination field."""
    tag: str = "100"
    name: str = "ExDestination"
    type: str = "EXCHANGE"
    value: FIXExchange
