
from .base import FIXFieldBase
from .types import FIXString

class LegIssuer(FIXFieldBase):
    """FIX LegIssuer field."""
    tag: str = "617"
    name: str = "LegIssuer"
    type: str = "STRING"
    value: FIXString
