
from .base import FIXFieldBase
from .types import FIXInt

class NestedPartyRole(FIXFieldBase):
    """FIX NestedPartyRole field."""
    tag: str = "538"
    name: str = "NestedPartyRole"
    type: str = "INT"
    value: FIXInt
