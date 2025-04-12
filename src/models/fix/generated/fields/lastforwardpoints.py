
from .base import FIXFieldBase
from .types import FIXString

class LastForwardPoints(FIXFieldBase):
    """FIX LastForwardPoints field."""
    tag: str = "195"
    name: str = "LastForwardPoints"
    type: str = "PRICEOFFSET"
    value: FIXString
