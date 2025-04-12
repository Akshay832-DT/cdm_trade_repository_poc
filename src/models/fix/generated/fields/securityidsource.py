
from .base import FIXFieldBase
from .types import FIXString

class SecurityIDSource(FIXFieldBase):
    """FIX SecurityIDSource field."""
    tag: str = "22"
    name: str = "SecurityIDSource"
    type: str = "STRING"
    value: FIXString

    # Enum values
    # 1: CUSIP
    # 2: SEDOL
    # 3: QUIK
    # 4: ISIN_NUMBER
    # 5: RIC_CODE
    # 6: ISO_CURRENCY_CODE
    # 7: ISO_COUNTRY_CODE
    # 8: EXCHANGE_SYMBOL
    # 9: CONSOLIDATED_TAPE_ASSOCIATION
    # A: BLOOMBERG_SYMBOL
    # B: WERTPAPIER
    # C: DUTCH
    # D: VALOREN
    # E: SICOVAM
    # F: BELGIAN
    # G: COMMON
    # H: CLEARING_HOUSE
    # I: ISDA_FP_ML_SPECIFICATION
    # J: OPTION_PRICE_REPORTING_AUTHORITY
