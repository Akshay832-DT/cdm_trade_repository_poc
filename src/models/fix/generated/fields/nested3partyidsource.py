
from .base import FIXFieldBase
from .types import FIXChar

class Nested3PartyIDSource(FIXFieldBase):
    """FIX Nested3PartyIDSource field."""
    tag: str = "950"
    name: str = "Nested3PartyIDSource"
    type: str = "CHAR"
    value: FIXChar
