
from .base import FIXFieldBase
from .types import FIXString

class RoutingID(FIXFieldBase):
    """FIX RoutingID field."""
    tag: str = "217"
    name: str = "RoutingID"
    type: str = "STRING"
    value: FIXString
