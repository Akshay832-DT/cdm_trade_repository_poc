
from .base import FIXFieldBase
from .types import FIXChar

class OrderCapacity(FIXFieldBase):
    """FIX OrderCapacity field."""
    tag: str = "528"
    name: str = "OrderCapacity"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # A: AGENCY
    # G: PROPRIETARY
    # I: INDIVIDUAL
    # P: PRINCIPAL
    # R: RISKLESS_PRINCIPAL
    # W: AGENT_FOR_OTHER_MEMBER
