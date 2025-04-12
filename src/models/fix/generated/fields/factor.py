
from .base import FIXFieldBase
from .types import FIXFloat

class Factor(FIXFieldBase):
    """FIX Factor field."""
    tag: str = "228"
    name: str = "Factor"
    type: str = "FLOAT"
    value: FIXFloat
