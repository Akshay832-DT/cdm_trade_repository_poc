
from .base import FIXFieldBase
from .types import FIXChar

class Nested2PartyIDSource(FIXFieldBase):
    """FIX Nested2PartyIDSource field."""
    tag: str = "758"
    name: str = "Nested2PartyIDSource"
    type: str = "CHAR"
    value: FIXChar
