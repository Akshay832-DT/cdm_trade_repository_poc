
from .base import FIXFieldBase
from .types import FIXChar

class DKReason(FIXFieldBase):
    """FIX DKReason field."""
    tag: str = "127"
    name: str = "DKReason"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # A: UNKNOWN_SYMBOL
    # B: WRONG_SIDE
    # C: QUANTITY_EXCEEDS_ORDER
    # D: NO_MATCHING_ORDER
    # E: PRICE_EXCEEDS_LIMIT
    # F: CALCULATION_DIFFERENCE
    # Z: OTHER
