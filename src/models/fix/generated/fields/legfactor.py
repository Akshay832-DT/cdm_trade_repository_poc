
from .base import FIXFieldBase
from .types import FIXFloat

class LegFactor(FIXFieldBase):
    """FIX LegFactor field."""
    tag: str = "253"
    name: str = "LegFactor"
    type: str = "FLOAT"
    value: FIXFloat
