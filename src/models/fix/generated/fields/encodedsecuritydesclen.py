
from .base import FIXFieldBase
from .types import FIXLength

class EncodedSecurityDescLen(FIXFieldBase):
    """FIX EncodedSecurityDescLen field."""
    tag: str = "350"
    name: str = "EncodedSecurityDescLen"
    type: str = "LENGTH"
    value: FIXLength
