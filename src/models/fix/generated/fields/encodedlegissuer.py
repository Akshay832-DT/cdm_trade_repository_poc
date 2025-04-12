
from .base import FIXFieldBase
from .types import FIXData

class EncodedLegIssuer(FIXFieldBase):
    """FIX EncodedLegIssuer field."""
    tag: str = "619"
    name: str = "EncodedLegIssuer"
    type: str = "DATA"
    value: FIXData
