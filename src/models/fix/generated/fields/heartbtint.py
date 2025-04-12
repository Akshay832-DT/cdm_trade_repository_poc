
from .base import FIXFieldBase
from .types import FIXInt

class HeartBtInt(FIXFieldBase):
    """FIX HeartBtInt field."""
    tag: str = "108"
    name: str = "HeartBtInt"
    type: str = "INT"
    value: FIXInt
