
from .base import FIXFieldBase
from .types import FIXString

class LegSecurityAltIDSource(FIXFieldBase):
    """FIX LegSecurityAltIDSource field."""
    tag: str = "606"
    name: str = "LegSecurityAltIDSource"
    type: str = "STRING"
    value: FIXString
