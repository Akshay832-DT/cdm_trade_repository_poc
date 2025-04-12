
from .base import FIXFieldBase
from .types import FIXInt

class NestedPartySubIDType(FIXFieldBase):
    """FIX NestedPartySubIDType field."""
    tag: str = "805"
    name: str = "NestedPartySubIDType"
    type: str = "INT"
    value: FIXInt
