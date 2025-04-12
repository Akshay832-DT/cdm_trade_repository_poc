
from .base import FIXFieldBase
from .types import FIXString

class LegSecurityAltID(FIXFieldBase):
    """FIX LegSecurityAltID field."""
    tag: str = "605"
    name: str = "LegSecurityAltID"
    type: str = "STRING"
    value: FIXString
