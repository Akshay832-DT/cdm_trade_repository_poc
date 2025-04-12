
from .base import FIXFieldBase
from .types import FIXString

class LegSecurityIDSource(FIXFieldBase):
    """FIX LegSecurityIDSource field."""
    tag: str = "603"
    name: str = "LegSecurityIDSource"
    type: str = "STRING"
    value: FIXString
