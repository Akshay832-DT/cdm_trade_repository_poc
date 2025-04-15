"""
FIX ExecPriceType field (tag 484).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ExecPriceTypeValues:
    """Enumerated values for ExecPriceType."""
    B = "B"  # BID_PRICE
    C = "C"  # CREATION_PRICE
    D = "D"  # CREATION_PRICE_PLUS_ADJUSTMENT_PERCENT
    E = "E"  # CREATION_PRICE_PLUS_ADJUSTMENT_AMOUNT
    O = "O"  # OFFER_PRICE
    P = "P"  # OFFER_PRICE_MINUS_ADJUSTMENT_PERCENT
    Q = "Q"  # OFFER_PRICE_MINUS_ADJUSTMENT_AMOUNT
    S = "S"  # SINGLE_PRICE

class ExecPriceTypeField(FIXFieldBase):
    """"""
    tag: str = "484"
    name: str = "ExecPriceType"
    type: str = "CHAR"
    value: Literal["B", "C", "D", "E", "O", "P", "Q", "S"]

    # Helper methods for enum values
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
    def is_o(self) -> bool:
        return self.value == "O"
    @property
    def is_p(self) -> bool:
        return self.value == "P"
    @property
    def is_q(self) -> bool:
        return self.value == "Q"
    @property
    def is_s(self) -> bool:
        return self.value == "S"
