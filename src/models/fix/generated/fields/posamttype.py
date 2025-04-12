
from .base import FIXFieldBase
from .types import FIXString

class PosAmtType(FIXFieldBase):
    """FIX PosAmtType field."""
    tag: str = "707"
    name: str = "PosAmtType"
    type: str = "STRING"
    value: FIXString

    # Enum values
    # FMTM: FINAL_MARK_TO_MARKET_AMOUNT
    # IMTM: INCREMENTAL_MARK_TO_MARKET_AMOUNT
    # TVAR: TRADE_VARIATION_AMOUNT
    # SMTM: START_OF_DAY_MARK_TO_MARKET_AMOUNT
    # PREM: PREMIUM_AMOUNT
    # CRES: CASH_RESIDUAL_AMOUNT
    # CASH: CASH_AMOUNT
    # VADJ: VALUE_ADJUSTED_AMOUNT
