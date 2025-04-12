
from .base import FIXFieldBase
from .types import FIXInt

class UnderlyingPutOrCall(FIXFieldBase):
    """FIX UnderlyingPutOrCall field."""
    tag: str = "315"
    name: str = "UnderlyingPutOrCall"
    type: str = "INT"
    value: FIXInt
