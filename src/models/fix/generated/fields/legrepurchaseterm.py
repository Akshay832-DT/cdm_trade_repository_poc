
from .base import FIXFieldBase
from .types import FIXInt

class LegRepurchaseTerm(FIXFieldBase):
    """FIX LegRepurchaseTerm field."""
    tag: str = "251"
    name: str = "LegRepurchaseTerm"
    type: str = "INT"
    value: FIXInt
