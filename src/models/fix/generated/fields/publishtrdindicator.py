
from .base import FIXFieldBase
from .types import FIXBoolean

class PublishTrdIndicator(FIXFieldBase):
    """FIX PublishTrdIndicator field."""
    tag: str = "852"
    name: str = "PublishTrdIndicator"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
