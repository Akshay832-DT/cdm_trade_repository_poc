
from .base import FIXFieldBase
from .types import FIXLength

class EncodedUnderlyingIssuerLen(FIXFieldBase):
    """FIX EncodedUnderlyingIssuerLen field."""
    tag: str = "362"
    name: str = "EncodedUnderlyingIssuerLen"
    type: str = "LENGTH"
    value: FIXLength
