
from .base import FIXFieldBase
from .types import FIXData

class EncodedIssuer(FIXFieldBase):
    """FIX EncodedIssuer field."""
    tag: str = "349"
    name: str = "EncodedIssuer"
    type: str = "DATA"
    value: FIXData
