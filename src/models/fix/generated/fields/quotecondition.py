"""
FIX QuoteCondition field (tag 276).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteConditionValues:
    """Enumerated values for QuoteCondition."""
    A = "A"  # OPEN
    B = "B"  # CLOSED
    C = "C"  # EXCHANGE_BEST
    D = "D"  # CONSOLIDATED_BEST
    E = "E"  # LOCKED
    F = "F"  # CROSSED
    G = "G"  # DEPTH
    H = "H"  # FAST_TRADING
    I = "I"  # NON_FIRM

class QuoteConditionField(FIXFieldBase):
    """"""
    tag: str = "276"
    name: str = "QuoteCondition"
    type: str = "MULTIPLEVALUESTRING"
    value: List[str]

    # Helper methods for enum values
    @property
    def is_a(self) -> bool:
        return self.value == "A"
    @property
    def is_b(self) -> bool:
        return self.value == "B"
    @property
    def is_c(self) -> bool:
        return self.value == "C"
    @property
    def is_d(self) -> bool:
        return self.value == "D"
    @property
    def is_e(self) -> bool:
        return self.value == "E"
    @property
    def is_f(self) -> bool:
        return self.value == "F"
    @property
    def is_g(self) -> bool:
        return self.value == "G"
    @property
    def is_h(self) -> bool:
        return self.value == "H"
    @property
    def is_i(self) -> bool:
        return self.value == "I"
