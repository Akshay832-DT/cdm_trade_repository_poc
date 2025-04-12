
from .base import FIXFieldBase
from .types import FIXLength

class EncodedIssuerLen(FIXFieldBase):
    """FIX EncodedIssuerLen field."""
    tag: str = "348"
    name: str = "EncodedIssuerLen"
    type: str = "LENGTH"
    value: FIXLength
