"""
FIX TradeCondition field (tag 277).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeConditionValues:
    """Enumerated values for TradeCondition."""
    A = "A"  # CASH
    B = "B"  # AVERAGE_PRICE_TRADE
    C = "C"  # CASH_TRADE
    D = "D"  # NEXT_DAY
    E = "E"  # OPENING
    F = "F"  # INTRADAY_TRADE_DETAIL
    G = "G"  # RULE127_TRADE
    H = "H"  # RULE155_TRADE
    I = "I"  # SOLD_LAST
    J = "J"  # NEXT_DAY_TRADE
    K = "K"  # OPENED
    L = "L"  # SELLER
    M = "M"  # SOLD
    N = "N"  # STOPPED_STOCK
    P = "P"  # IMBALANCE_MORE_BUYERS
    Q = "Q"  # IMBALANCE_MORE_SELLERS
    R = "R"  # OPENING_PRICE

class TradeConditionField(FIXFieldBase):
    """"""
    tag: str = "277"
    name: str = "TradeCondition"
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
    @property
    def is_j(self) -> bool:
        return self.value == "J"
    @property
    def is_k(self) -> bool:
        return self.value == "K"
    @property
    def is_l(self) -> bool:
        return self.value == "L"
    @property
    def is_m(self) -> bool:
        return self.value == "M"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
    @property
    def is_p(self) -> bool:
        return self.value == "P"
    @property
    def is_q(self) -> bool:
        return self.value == "Q"
    @property
    def is_r(self) -> bool:
        return self.value == "R"
