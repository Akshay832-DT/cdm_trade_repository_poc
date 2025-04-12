
from .base import FIXFieldBase
from .types import FIXData

class SecureData(FIXFieldBase):
    """FIX SecureData field."""
    tag: str = "91"
    name: str = "SecureData"
    type: str = "DATA"
    value: FIXData
