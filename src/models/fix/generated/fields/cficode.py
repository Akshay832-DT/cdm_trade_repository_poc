
from .base import FIXFieldBase
from .types import FIXString

class CFICode(FIXFieldBase):
    """FIX CFICode field."""
    tag: str = "461"
    name: str = "CFICode"
    type: str = "STRING"
    value: FIXString
