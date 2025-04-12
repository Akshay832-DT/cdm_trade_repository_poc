
from .base import FIXFieldBase
from .types import FIXString

class AgreementID(FIXFieldBase):
    """FIX AgreementID field."""
    tag: str = "914"
    name: str = "AgreementID"
    type: str = "STRING"
    value: FIXString
