
from .base import FIXFieldBase
from .types import FIXBoolean

class NotifyBrokerOfCredit(FIXFieldBase):
    """FIX NotifyBrokerOfCredit field."""
    tag: str = "208"
    name: str = "NotifyBrokerOfCredit"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
