
from .base import FIXFieldBase
from .types import FIXInt

class UnderlyingProduct(FIXFieldBase):
    """FIX UnderlyingProduct field."""
    tag: str = "462"
    name: str = "UnderlyingProduct"
    type: str = "INT"
    value: FIXInt
