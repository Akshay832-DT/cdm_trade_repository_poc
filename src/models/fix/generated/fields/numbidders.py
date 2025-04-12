
from .base import FIXFieldBase
from .types import FIXInt

class NumBidders(FIXFieldBase):
    """FIX NumBidders field."""
    tag: str = "417"
    name: str = "NumBidders"
    type: str = "INT"
    value: FIXInt
