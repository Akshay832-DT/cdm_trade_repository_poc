
from .base import FIXFieldBase
from .types import FIXBoolean

class PriorSpreadIndicator(FIXFieldBase):
    """FIX PriorSpreadIndicator field."""
    tag: str = "720"
    name: str = "PriorSpreadIndicator"
    type: str = "BOOLEAN"
    value: FIXBoolean
