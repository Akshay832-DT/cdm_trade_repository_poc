
from .base import FIXFieldBase
from .types import FIXInt

class TotalAffectedOrders(FIXFieldBase):
    """FIX TotalAffectedOrders field."""
    tag: str = "533"
    name: str = "TotalAffectedOrders"
    type: str = "INT"
    value: FIXInt
