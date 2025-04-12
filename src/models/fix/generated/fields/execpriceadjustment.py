
from .base import FIXFieldBase
from .types import FIXFloat

class ExecPriceAdjustment(FIXFieldBase):
    """FIX ExecPriceAdjustment field."""
    tag: str = "485"
    name: str = "ExecPriceAdjustment"
    type: str = "FLOAT"
    value: FIXFloat
