
from .base import FIXFieldBase
from .types import FIXString

class LegSecuritySubType(FIXFieldBase):
    """FIX LegSecuritySubType field."""
    tag: str = "764"
    name: str = "LegSecuritySubType"
    type: str = "STRING"
    value: FIXString
