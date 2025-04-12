
from .base import FIXFieldBase
from .types import FIXBoolean

class ForexReq(FIXFieldBase):
    """FIX ForexReq field."""
    tag: str = "121"
    name: str = "ForexReq"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
