
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingCPRegType(FIXFieldBase):
    """FIX UnderlyingCPRegType field."""
    tag: str = "878"
    name: str = "UnderlyingCPRegType"
    type: str = "STRING"
    value: FIXString
