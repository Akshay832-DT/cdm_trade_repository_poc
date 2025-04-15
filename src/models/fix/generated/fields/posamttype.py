"""
FIX PosAmtType field (tag 707).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PosAmtTypeValues:
    """Enumerated values for PosAmtType."""
    FMTM = "FMTM"  # FINAL_MARK_TO_MARKET_AMOUNT
    IMTM = "IMTM"  # INCREMENTAL_MARK_TO_MARKET_AMOUNT
    TVAR = "TVAR"  # TRADE_VARIATION_AMOUNT
    SMTM = "SMTM"  # START_OF_DAY_MARK_TO_MARKET_AMOUNT
    PREM = "PREM"  # PREMIUM_AMOUNT
    CRES = "CRES"  # CASH_RESIDUAL_AMOUNT
    CASH = "CASH"  # CASH_AMOUNT
    VADJ = "VADJ"  # VALUE_ADJUSTED_AMOUNT

class PosAmtTypeField(FIXFieldBase):
    """"""
    tag: str = "707"
    name: str = "PosAmtType"
    type: str = "STRING"
    value: Literal["FMTM", "IMTM", "TVAR", "SMTM", "PREM", "CRES", "CASH", "VADJ"]

    # Helper methods for enum values
    @property
    def is_fmtm(self) -> bool:
        return self.value == "FMTM"
    @property
    def is_imtm(self) -> bool:
        return self.value == "IMTM"
    @property
    def is_tvar(self) -> bool:
        return self.value == "TVAR"
    @property
    def is_smtm(self) -> bool:
        return self.value == "SMTM"
    @property
    def is_prem(self) -> bool:
        return self.value == "PREM"
    @property
    def is_cres(self) -> bool:
        return self.value == "CRES"
    @property
    def is_cash(self) -> bool:
        return self.value == "CASH"
    @property
    def is_vadj(self) -> bool:
        return self.value == "VADJ"
