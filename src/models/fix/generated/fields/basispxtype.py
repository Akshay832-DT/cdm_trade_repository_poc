"""
FIX BasisPxType field (tag 419).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BasisPxTypeValues:
    """Enumerated values for BasisPxType."""
    VALUE_2 = "2"  # CLOSING_PRICE_AT_MORNING_SESSION
    VALUE_3 = "3"  # CLOSING_PRICE
    VALUE_4 = "4"  # CURRENT_PRICE
    VALUE_5 = "5"  # SQ
    VALUE_6 = "6"  # VWAP_THROUGH_A_DAY
    VALUE_7 = "7"  # VWAP_THROUGH_A_MORNING_SESSION
    VALUE_8 = "8"  # VWAP_THROUGH_AN_AFTERNOON_SESSION
    VALUE_9 = "9"  # VWAP_THROUGH_A_DAY_EXCEPT
    A = "A"  # VWAP_THROUGH_A_MORNING_SESSION_EXCEPT
    B = "B"  # VWAP_THROUGH_AN_AFTERNOON_SESSION_EXCEPT
    C = "C"  # STRIKE
    D = "D"  # OPEN
    Z = "Z"  # OTHERS

class BasisPxTypeField(FIXFieldBase):
    """"""
    tag: str = "419"
    name: str = "BasisPxType"
    type: str = "CHAR"
    value: Literal["2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "Z"]

    # Helper methods for enum values
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
    def is_z(self) -> bool:
        return self.value == "Z"
