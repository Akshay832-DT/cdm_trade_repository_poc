
from .base import FIXFieldBase
from .types import FIXString

class LastForwardPoints2(FIXFieldBase):
    """FIX LastForwardPoints2 field."""
    tag: str = "641"
    name: str = "LastForwardPoints2"
    type: str = "PRICEOFFSET"
    value: FIXString
