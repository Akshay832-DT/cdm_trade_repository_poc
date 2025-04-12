
from .base import FIXFieldBase
from .types import FIXString

class IOIRefID(FIXFieldBase):
    """FIX IOIRefID field."""
    tag: str = "26"
    name: str = "IOIRefID"
    type: str = "STRING"
    value: FIXString
