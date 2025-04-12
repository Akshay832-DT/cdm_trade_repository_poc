
from .base import FIXFieldBase
from .types import FIXString

class RegistAcctType(FIXFieldBase):
    """FIX RegistAcctType field."""
    tag: str = "493"
    name: str = "RegistAcctType"
    type: str = "STRING"
    value: FIXString
