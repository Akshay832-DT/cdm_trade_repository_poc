
from .base import FIXFieldBase
from .types import FIXData

class XmlData(FIXFieldBase):
    """FIX XmlData field."""
    tag: str = "213"
    name: str = "XmlData"
    type: str = "DATA"
    value: FIXData
