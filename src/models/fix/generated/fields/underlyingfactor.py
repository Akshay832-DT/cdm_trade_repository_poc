
from .base import FIXFieldBase
from .types import FIXFloat

class UnderlyingFactor(FIXFieldBase):
    """FIX UnderlyingFactor field."""
    tag: str = "246"
    name: str = "UnderlyingFactor"
    type: str = "FLOAT"
    value: FIXFloat
