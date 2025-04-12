
from .base import FIXFieldBase
from .types import FIXChar

class BidRequestTransType(FIXFieldBase):
    """FIX BidRequestTransType field."""
    tag: str = "374"
    name: str = "BidRequestTransType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # N: NEW
    # C: CANCEL
