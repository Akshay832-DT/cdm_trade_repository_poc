
from .base import FIXFieldBase
from .types import FIXChar

class FundRenewWaiv(FIXFieldBase):
    """FIX FundRenewWaiv field."""
    tag: str = "497"
    name: str = "FundRenewWaiv"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # Y: YES
    # N: NO
