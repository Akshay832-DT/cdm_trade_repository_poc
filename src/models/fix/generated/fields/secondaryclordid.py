
from .base import FIXFieldBase
from .types import FIXString

class SecondaryClOrdID(FIXFieldBase):
    """FIX SecondaryClOrdID field."""
    tag: str = "526"
    name: str = "SecondaryClOrdID"
    type: str = "STRING"
    value: FIXString
