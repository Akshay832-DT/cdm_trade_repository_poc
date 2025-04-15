"""
FIX ExecInst field (tag 18).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ExecInstValues:
    """Enumerated values for ExecInst."""
    VALUE_1 = "1"  # NOT_HELD
    VALUE_2 = "2"  # WORK
    VALUE_3 = "3"  # GO_ALONG
    VALUE_4 = "4"  # OVER_THE_DAY
    VALUE_5 = "5"  # HELD
    VALUE_6 = "6"  # PARTICIPATE_DO_NOT_INITIATE
    VALUE_7 = "7"  # STRICT_SCALE
    VALUE_8 = "8"  # TRY_TO_SCALE
    VALUE_9 = "9"  # STAY_ON_BID_SIDE
    VALUE_0 = "0"  # STAY_ON_OFFER_SIDE
    A = "A"  # NO_CROSS
    B = "B"  # OK_TO_CROSS
    C = "C"  # CALL_FIRST
    D = "D"  # PERCENT_OF_VOLUME
    E = "E"  # DO_NOT_INCREASE
    F = "F"  # DO_NOT_REDUCE
    G = "G"  # ALL_OR_NONE
    H = "H"  # REINSTATE_ON_SYSTEM_FAILURE
    I = "I"  # INSTITUTIONS_ONLY
    J = "J"  # REINSTATE_ON_TRADING_HALT
    K = "K"  # CANCEL_ON_TRADING_HALT
    L = "L"  # LAST_PEG
    M = "M"  # MID_PRICE_PEG
    N = "N"  # NON_NEGOTIABLE
    O = "O"  # OPENING_PEG
    P = "P"  # MARKET_PEG
    Q = "Q"  # CANCEL_ON_SYSTEM_FAILURE
    R = "R"  # PRIMARY_PEG
    S = "S"  # SUSPEND
    U = "U"  # CUSTOMER_DISPLAY_INSTRUCTION
    V = "V"  # NETTING
    W = "W"  # PEG_TO_VWAP
    X = "X"  # TRADE_ALONG
    Y = "Y"  # TRY_TO_STOP
    Z = "Z"  # CANCEL_IF_NOT_BEST
    a = "a"  # TRAILING_STOP_PEG
    b = "b"  # STRICT_LIMIT
    c = "c"  # IGNORE_PRICE_VALIDITY_CHECKS
    d = "d"  # PEG_TO_LIMIT_PRICE
    e = "e"  # WORK_TO_TARGET_STRATEGY

class ExecInstField(FIXFieldBase):
    """"""
    tag: str = "18"
    name: str = "ExecInst"
    type: str = "MULTIPLEVALUESTRING"
    value: List[str]

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
    def is_value_0(self) -> bool:
        return self.value == "0"
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
    def is_u(self) -> bool:
        return self.value == "U"
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
    @property
    def is_a(self) -> bool:
        return self.value == "a"
    @property
    def is_b(self) -> bool:
        return self.value == "b"
    @property
    def is_c(self) -> bool:
        return self.value == "c"
    @property
    def is_d(self) -> bool:
        return self.value == "d"
    @property
    def is_e(self) -> bool:
        return self.value == "e"
