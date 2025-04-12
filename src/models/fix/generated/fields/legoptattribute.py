
from .base import FIXFieldBase
from .types import FIXChar

class LegOptAttribute(FIXFieldBase):
    """FIX LegOptAttribute field."""
    tag: str = "613"
    name: str = "LegOptAttribute"
    type: str = "CHAR"
    value: FIXChar
