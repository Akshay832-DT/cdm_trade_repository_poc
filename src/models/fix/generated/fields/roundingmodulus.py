
from .base import FIXFieldBase
from .types import FIXFloat

class RoundingModulus(FIXFieldBase):
    """FIX RoundingModulus field."""
    tag: str = "469"
    name: str = "RoundingModulus"
    type: str = "FLOAT"
    value: FIXFloat
