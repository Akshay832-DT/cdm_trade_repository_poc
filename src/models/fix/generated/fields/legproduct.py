
from .base import FIXFieldBase
from .types import FIXInt

class LegProduct(FIXFieldBase):
    """FIX LegProduct field."""
    tag: str = "607"
    name: str = "LegProduct"
    type: str = "INT"
    value: FIXInt
