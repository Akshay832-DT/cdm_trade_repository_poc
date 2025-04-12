
from .base import FIXFieldBase
from .types import FIXInt

class Nested3PartyRole(FIXFieldBase):
    """FIX Nested3PartyRole field."""
    tag: str = "951"
    name: str = "Nested3PartyRole"
    type: str = "INT"
    value: FIXInt
