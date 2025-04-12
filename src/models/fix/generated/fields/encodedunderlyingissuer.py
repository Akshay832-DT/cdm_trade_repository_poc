
from .base import FIXFieldBase
from .types import FIXData

class EncodedUnderlyingIssuer(FIXFieldBase):
    """FIX EncodedUnderlyingIssuer field."""
    tag: str = "363"
    name: str = "EncodedUnderlyingIssuer"
    type: str = "DATA"
    value: FIXData
