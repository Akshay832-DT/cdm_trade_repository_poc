"""
FIX OrdType field (tag 40).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrdTypeValues:
    """Enumerated values for OrdType."""
    VALUE_1 = "1"  # MARKET
    VALUE_2 = "2"  # LIMIT
    VALUE_3 = "3"  # STOP
    VALUE_4 = "4"  # STOP_LIMIT
    VALUE_6 = "6"  # WITH_OR_WITHOUT
    VALUE_7 = "7"  # LIMIT_OR_BETTER
    VALUE_8 = "8"  # LIMIT_WITH_OR_WITHOUT
    VALUE_9 = "9"  # ON_BASIS
    D = "D"  # PREVIOUSLY_QUOTED
    E = "E"  # PREVIOUSLY_INDICATED
    G = "G"  # FOREX_SWAP
    I = "I"  # FUNARI
    J = "J"  # MARKET_IF_TOUCHED
    K = "K"  # MARKET_WITH_LEFT_OVER_AS_LIMIT
    L = "L"  # PREVIOUS_FUND_VALUATION_POINT
    M = "M"  # NEXT_FUND_VALUATION_POINT
    P = "P"  # PEGGED

class OrdTypeField(FIXFieldBase):
    """"""
    tag: str = "40"
    name: str = "OrdType"
    type: str = "CHAR"
    value: Literal["1", "2", "3", "4", "6", "7", "8", "9", "D", "E", "G", "I", "J", "K", "L", "M", "P"]

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
    def is_d(self) -> bool:
        return self.value == "D"
    @property
    def is_e(self) -> bool:
        return self.value == "E"
    @property
    def is_g(self) -> bool:
        return self.value == "G"
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
    def is_p(self) -> bool:
        return self.value == "P"
