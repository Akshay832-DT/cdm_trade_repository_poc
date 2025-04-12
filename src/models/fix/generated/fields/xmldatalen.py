
from .base import FIXFieldBase
from .types import FIXLength

class XmlDataLen(FIXFieldBase):
    """FIX XmlDataLen field."""
    tag: str = "212"
    name: str = "XmlDataLen"
    type: str = "LENGTH"
    value: FIXLength
