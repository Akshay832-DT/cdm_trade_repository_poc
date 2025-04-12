
from .base import FIXFieldBase
from .types import FIXBoolean

class TestMessageIndicator(FIXFieldBase):
    """FIX TestMessageIndicator field."""
    tag: str = "464"
    name: str = "TestMessageIndicator"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
