
from .base import FIXFieldBase
from .types import FIXData

class EncodedUnderlyingSecurityDesc(FIXFieldBase):
    """FIX EncodedUnderlyingSecurityDesc field."""
    tag: str = "365"
    name: str = "EncodedUnderlyingSecurityDesc"
    type: str = "DATA"
    value: FIXData
