"""
FIX IOIQualifier field (tag 104).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class IOIQualifierValues:
    """Enumerated values for IOIQualifier."""
    A = "A"  # ALL_OR_NONE
    B = "B"  # MARKET_ON_CLOSE
    C = "C"  # AT_THE_CLOSE
    D = "D"  # VWAP
    I = "I"  # IN_TOUCH_WITH
    L = "L"  # LIMIT
    M = "M"  # MORE_BEHIND
    O = "O"  # AT_THE_OPEN
    P = "P"  # TAKING_A_POSITION
    Q = "Q"  # AT_THE_MARKET
    R = "R"  # READY_TO_TRADE
    S = "S"  # PORTFOLIO_SHOWN
    T = "T"  # THROUGH_THE_DAY
    V = "V"  # VERSUS
    W = "W"  # INDICATION
    X = "X"  # CROSSING_OPPORTUNITY
    Y = "Y"  # AT_THE_MIDPOINT
    Z = "Z"  # PRE_OPEN

class IOIQualifierField(FIXFieldBase):
    """"""
    tag: str = "104"
    name: str = "IOIQualifier"
    type: str = "CHAR"
    value: Literal["A", "B", "C", "D", "I", "L", "M", "O", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

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
    def is_i(self) -> bool:
        return self.value == "I"
    @property
    def is_l(self) -> bool:
        return self.value == "L"
    @property
    def is_m(self) -> bool:
        return self.value == "M"
    @property
    def is_o(self) -> bool:
        return self.value == "O"
    @property
    def is_p(self) -> bool:
        return self.value == "P"
    @property
    def is_q(self) -> bool:
        return self.value == "Q"
    @property
    def is_r(self) -> bool:
        return self.value == "R"
    @property
    def is_s(self) -> bool:
        return self.value == "S"
    @property
    def is_t(self) -> bool:
        return self.value == "T"
    @property
    def is_v(self) -> bool:
        return self.value == "V"
    @property
    def is_w(self) -> bool:
        return self.value == "W"
    @property
    def is_x(self) -> bool:
        return self.value == "X"
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_z(self) -> bool:
        return self.value == "Z"
