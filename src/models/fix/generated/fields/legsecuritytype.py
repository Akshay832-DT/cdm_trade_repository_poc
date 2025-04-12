
from .base import FIXFieldBase
from .types import FIXString

class LegSecurityType(FIXFieldBase):
    """FIX LegSecurityType field."""
    tag: str = "609"
    name: str = "LegSecurityType"
    type: str = "STRING"
    value: FIXString
