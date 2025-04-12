
from .base import FIXFieldBase
from .types import FIXChar

class SettlCurrFxRateCalc(FIXFieldBase):
    """FIX SettlCurrFxRateCalc field."""
    tag: str = "156"
    name: str = "SettlCurrFxRateCalc"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # M: MULTIPLY
    # D: DIVIDE
