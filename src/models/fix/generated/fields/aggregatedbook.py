
from .base import FIXFieldBase
from .types import FIXBoolean

class AggregatedBook(FIXFieldBase):
    """FIX AggregatedBook field."""
    tag: str = "266"
    name: str = "AggregatedBook"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
