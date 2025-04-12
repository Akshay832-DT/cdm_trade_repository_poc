
from .base import FIXFieldBase
from .types import FIXMultipleValueString

class QuoteCondition(FIXFieldBase):
    """FIX QuoteCondition field."""
    tag: str = "276"
    name: str = "QuoteCondition"
    type: str = "MULTIPLEVALUESTRING"
    value: FIXMultipleValueString

    # Enum values
    # A: OPEN
    # B: CLOSED
    # C: EXCHANGE_BEST
    # D: CONSOLIDATED_BEST
    # E: LOCKED
    # F: CROSSED
    # G: DEPTH
    # H: FAST_TRADING
    # I: NON_FIRM
