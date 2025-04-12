
from .base import FIXFieldBase
from .types import FIXString

class LegSecurityID(FIXFieldBase):
    """FIX LegSecurityID field."""
    tag: str = "602"
    name: str = "LegSecurityID"
    type: str = "STRING"
    value: FIXString
