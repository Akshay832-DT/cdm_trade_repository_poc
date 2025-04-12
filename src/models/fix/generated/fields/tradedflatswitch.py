
from .base import FIXFieldBase
from .types import FIXBoolean

class TradedFlatSwitch(FIXFieldBase):
    """FIX TradedFlatSwitch field."""
    tag: str = "258"
    name: str = "TradedFlatSwitch"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
