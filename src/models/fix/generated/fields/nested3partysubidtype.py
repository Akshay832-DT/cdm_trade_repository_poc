
from .base import FIXFieldBase
from .types import FIXInt

class Nested3PartySubIDType(FIXFieldBase):
    """FIX Nested3PartySubIDType field."""
    tag: str = "954"
    name: str = "Nested3PartySubIDType"
    type: str = "INT"
    value: FIXInt
