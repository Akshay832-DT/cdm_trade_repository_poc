
from .base import FIXFieldBase
from .types import FIXData

class EncodedSecurityDesc(FIXFieldBase):
    """FIX EncodedSecurityDesc field."""
    tag: str = "351"
    name: str = "EncodedSecurityDesc"
    type: str = "DATA"
    value: FIXData
