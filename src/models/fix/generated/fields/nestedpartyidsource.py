
from .base import FIXFieldBase
from .types import FIXChar

class NestedPartyIDSource(FIXFieldBase):
    """FIX NestedPartyIDSource field."""
    tag: str = "525"
    name: str = "NestedPartyIDSource"
    type: str = "CHAR"
    value: FIXChar
