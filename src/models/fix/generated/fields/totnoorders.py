
from .base import FIXFieldBase
from .types import FIXInt

class TotNoOrders(FIXFieldBase):
    """FIX TotNoOrders field."""
    tag: str = "68"
    name: str = "TotNoOrders"
    type: str = "INT"
    value: FIXInt
