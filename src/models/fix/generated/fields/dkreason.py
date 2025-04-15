"""
FIX DKReason field (tag 127).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DKReasonValues:
    """Enumerated values for DKReason."""
    A = "A"  # UNKNOWN_SYMBOL
    B = "B"  # WRONG_SIDE
    C = "C"  # QUANTITY_EXCEEDS_ORDER
    D = "D"  # NO_MATCHING_ORDER
    E = "E"  # PRICE_EXCEEDS_LIMIT
    F = "F"  # CALCULATION_DIFFERENCE
    Z = "Z"  # OTHER

class DKReasonField(FIXFieldBase):
    """"""
    tag: str = "127"
    name: str = "DKReason"
    type: str = "CHAR"
    value: Literal["A", "B", "C", "D", "E", "F", "Z"]

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
    def is_z(self) -> bool:
        return self.value == "Z"
