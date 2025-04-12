
from .base import FIXFieldBase
from .types import FIXString

class LegSecurityDesc(FIXFieldBase):
    """FIX LegSecurityDesc field."""
    tag: str = "620"
    name: str = "LegSecurityDesc"
    type: str = "STRING"
    value: FIXString
