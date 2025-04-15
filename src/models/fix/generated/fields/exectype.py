"""
FIX ExecType field (tag 150).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ExecTypeValues:
    """Enumerated values for ExecType."""
    VALUE_0 = "0"  # NEW
    VALUE_3 = "3"  # DONE_FOR_DAY
    VALUE_4 = "4"  # CANCELED
    VALUE_5 = "5"  # REPLACED
    VALUE_6 = "6"  # PENDING_CANCEL
    VALUE_7 = "7"  # STOPPED
    VALUE_8 = "8"  # REJECTED
    VALUE_9 = "9"  # SUSPENDED
    A = "A"  # PENDING_NEW
    B = "B"  # CALCULATED
    C = "C"  # EXPIRED
    D = "D"  # RESTATED
    E = "E"  # PENDING_REPLACE
    F = "F"  # TRADE
    G = "G"  # TRADE_CORRECT
    H = "H"  # TRADE_CANCEL
    I = "I"  # ORDER_STATUS

class ExecTypeField(FIXFieldBase):
    """"""
    tag: str = "150"
    name: str = "ExecType"
    type: str = "CHAR"
    value: Literal["0", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
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
    @property
    def is_h(self) -> bool:
        return self.value == "H"
    @property
    def is_i(self) -> bool:
        return self.value == "I"
