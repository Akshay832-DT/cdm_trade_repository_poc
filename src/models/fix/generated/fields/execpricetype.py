
from .base import FIXFieldBase
from .types import FIXChar

class ExecPriceType(FIXFieldBase):
    """FIX ExecPriceType field."""
    tag: str = "484"
    name: str = "ExecPriceType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # B: BID_PRICE
    # C: CREATION_PRICE
    # D: CREATION_PRICE_PLUS_ADJUSTMENT_PERCENT
    # E: CREATION_PRICE_PLUS_ADJUSTMENT_AMOUNT
    # O: OFFER_PRICE
    # P: OFFER_PRICE_MINUS_ADJUSTMENT_PERCENT
    # Q: OFFER_PRICE_MINUS_ADJUSTMENT_AMOUNT
    # S: SINGLE_PRICE
