
from .base import FIXFieldBase
from .types import FIXInt

class SecondaryTrdType(FIXFieldBase):
    """FIX SecondaryTrdType field."""
    tag: str = "855"
    name: str = "SecondaryTrdType"
    type: str = "INT"
    value: FIXInt
