
from .base import FIXFieldBase
from .types import FIXInt

class Nested2PartySubIDType(FIXFieldBase):
    """FIX Nested2PartySubIDType field."""
    tag: str = "807"
    name: str = "Nested2PartySubIDType"
    type: str = "INT"
    value: FIXInt
