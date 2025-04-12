
from .base import FIXFieldBase
from .types import FIXString

class SettlSessID(FIXFieldBase):
    """FIX SettlSessID field."""
    tag: str = "716"
    name: str = "SettlSessID"
    type: str = "STRING"
    value: FIXString

    # Enum values
    # ITD: INTRADAY
    # RTH: REGULAR_TRADING_HOURS
    # ETH: ELECTRONIC_TRADING_HOURS
