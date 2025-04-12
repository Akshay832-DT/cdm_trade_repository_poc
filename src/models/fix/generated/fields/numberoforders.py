
from .base import FIXFieldBase
from .types import FIXInt

class NumberOfOrders(FIXFieldBase):
    """FIX NumberOfOrders field."""
    tag: str = "346"
    name: str = "NumberOfOrders"
    type: str = "INT"
    value: FIXInt
