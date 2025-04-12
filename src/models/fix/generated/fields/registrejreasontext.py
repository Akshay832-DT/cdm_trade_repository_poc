
from .base import FIXFieldBase
from .types import FIXString

class RegistRejReasonText(FIXFieldBase):
    """FIX RegistRejReasonText field."""
    tag: str = "496"
    name: str = "RegistRejReasonText"
    type: str = "STRING"
    value: FIXString
