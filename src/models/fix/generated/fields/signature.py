
from .base import FIXFieldBase
from .types import FIXData

class Signature(FIXFieldBase):
    """FIX Signature field."""
    tag: str = "89"
    name: str = "Signature"
    type: str = "DATA"
    value: FIXData
