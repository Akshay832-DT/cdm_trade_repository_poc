
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingIssuer(FIXFieldBase):
    """FIX UnderlyingIssuer field."""
    tag: str = "306"
    name: str = "UnderlyingIssuer"
    type: str = "STRING"
    value: FIXString
