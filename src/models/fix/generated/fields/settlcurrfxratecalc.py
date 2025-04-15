"""
FIX SettlCurrFxRateCalc field (tag 156).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlCurrFxRateCalcValues:
    """Enumerated values for SettlCurrFxRateCalc."""
    M = "M"  # MULTIPLY
    D = "D"  # DIVIDE

class SettlCurrFxRateCalcField(FIXFieldBase):
    """"""
    tag: str = "156"
    name: str = "SettlCurrFxRateCalc"
    type: str = "CHAR"
    value: Literal["M", "D"]

    # Helper methods for enum values
    @property
    def is_m(self) -> bool:
        return self.value == "M"
    @property
    def is_d(self) -> bool:
        return self.value == "D"
