
from .base import FIXFieldBase
from .types import FIXBoolean

class LegalConfirm(FIXFieldBase):
    """FIX LegalConfirm field."""
    tag: str = "650"
    name: str = "LegalConfirm"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
