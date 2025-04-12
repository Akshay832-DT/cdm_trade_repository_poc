
from .base import FIXFieldBase
from .types import FIXLength

class EncodedUnderlyingSecurityDescLen(FIXFieldBase):
    """FIX EncodedUnderlyingSecurityDescLen field."""
    tag: str = "364"
    name: str = "EncodedUnderlyingSecurityDescLen"
    type: str = "LENGTH"
    value: FIXLength
