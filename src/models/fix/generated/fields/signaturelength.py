
from .base import FIXFieldBase
from .types import FIXLength

class SignatureLength(FIXFieldBase):
    """FIX SignatureLength field."""
    tag: str = "93"
    name: str = "SignatureLength"
    type: str = "LENGTH"
    value: FIXLength
