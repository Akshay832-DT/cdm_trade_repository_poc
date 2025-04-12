
from .base import FIXFieldBase
from .types import FIXLength

class EncodedLegSecurityDescLen(FIXFieldBase):
    """FIX EncodedLegSecurityDescLen field."""
    tag: str = "621"
    name: str = "EncodedLegSecurityDescLen"
    type: str = "LENGTH"
    value: FIXLength
