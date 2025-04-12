
from .base import FIXFieldBase
from .types import FIXData

class EncodedLegSecurityDesc(FIXFieldBase):
    """FIX EncodedLegSecurityDesc field."""
    tag: str = "622"
    name: str = "EncodedLegSecurityDesc"
    type: str = "DATA"
    value: FIXData
