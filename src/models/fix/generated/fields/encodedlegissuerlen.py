
from .base import FIXFieldBase
from .types import FIXLength

class EncodedLegIssuerLen(FIXFieldBase):
    """FIX EncodedLegIssuerLen field."""
    tag: str = "618"
    name: str = "EncodedLegIssuerLen"
    type: str = "LENGTH"
    value: FIXLength
