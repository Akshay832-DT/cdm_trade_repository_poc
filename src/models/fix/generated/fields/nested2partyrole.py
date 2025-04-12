
from .base import FIXFieldBase
from .types import FIXInt

class Nested2PartyRole(FIXFieldBase):
    """FIX Nested2PartyRole field."""
    tag: str = "759"
    name: str = "Nested2PartyRole"
    type: str = "INT"
    value: FIXInt
