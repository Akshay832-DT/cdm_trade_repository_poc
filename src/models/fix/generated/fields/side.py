"""
FIX Side field (tag 54).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SideValues:
    """Enumerated values for Side."""
    VALUE_1 = "1"  # BUY
    VALUE_2 = "2"  # SELL
    VALUE_3 = "3"  # BUY_MINUS
    VALUE_4 = "4"  # SELL_PLUS
    VALUE_5 = "5"  # SELL_SHORT
    VALUE_6 = "6"  # SELL_SHORT_EXEMPT
    VALUE_7 = "7"  # UNDISCLOSED
    VALUE_8 = "8"  # CROSS
    VALUE_9 = "9"  # CROSS_SHORT
    A = "A"  # CROSS_SHORT_EXEMPT
    B = "B"  # AS_DEFINED
    C = "C"  # OPPOSITE
    D = "D"  # SUBSCRIBE
    E = "E"  # REDEEM
    F = "F"  # LEND
    G = "G"  # BORROW

class SideField(FIXFieldBase):
    """"""
    tag: str = "54"
    name: str = "Side"
    type: str = "CHAR"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
    @property
    def is_value_3(self) -> bool:
        return self.value == "3"
    @property
    def is_value_4(self) -> bool:
        return self.value == "4"
    @property
    def is_value_5(self) -> bool:
        return self.value == "5"
    @property
    def is_value_6(self) -> bool:
        return self.value == "6"
    @property
    def is_value_7(self) -> bool:
        return self.value == "7"
    @property
    def is_value_8(self) -> bool:
        return self.value == "8"
    @property
    def is_value_9(self) -> bool:
        return self.value == "9"
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
