
from .base import FIXFieldBase
from .types import FIXInt

class UnderlyingRepurchaseTerm(FIXFieldBase):
    """FIX UnderlyingRepurchaseTerm field."""
    tag: str = "244"
    name: str = "UnderlyingRepurchaseTerm"
    type: str = "INT"
    value: FIXInt
