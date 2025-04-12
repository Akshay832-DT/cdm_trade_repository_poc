
from .base import FIXFieldBase
from .types import FIXString

class Issuer(FIXFieldBase):
    """FIX Issuer field."""
    tag: str = "106"
    name: str = "Issuer"
    type: str = "STRING"
    value: FIXString
