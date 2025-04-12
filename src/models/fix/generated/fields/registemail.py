
from .base import FIXFieldBase
from .types import FIXString

class RegistEmail(FIXFieldBase):
    """FIX RegistEmail field."""
    tag: str = "511"
    name: str = "RegistEmail"
    type: str = "STRING"
    value: FIXString
