
from .base import FIXFieldBase
from .types import FIXString

class AltMDSourceID(FIXFieldBase):
    """FIX AltMDSourceID field."""
    tag: str = "817"
    name: str = "AltMDSourceID"
    type: str = "STRING"
    value: FIXString
