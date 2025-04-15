"""
FIX SecurityIDSource field (tag 22).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecurityIDSourceValues:
    """Enumerated values for SecurityIDSource."""
    VALUE_1 = "1"  # CUSIP
    VALUE_2 = "2"  # SEDOL
    VALUE_3 = "3"  # QUIK
    VALUE_4 = "4"  # ISIN_NUMBER
    VALUE_5 = "5"  # RIC_CODE
    VALUE_6 = "6"  # ISO_CURRENCY_CODE
    VALUE_7 = "7"  # ISO_COUNTRY_CODE
    VALUE_8 = "8"  # EXCHANGE_SYMBOL
    VALUE_9 = "9"  # CONSOLIDATED_TAPE_ASSOCIATION
    A = "A"  # BLOOMBERG_SYMBOL
    B = "B"  # WERTPAPIER
    C = "C"  # DUTCH
    D = "D"  # VALOREN
    E = "E"  # SICOVAM
    F = "F"  # BELGIAN
    G = "G"  # COMMON
    H = "H"  # CLEARING_HOUSE
    I = "I"  # ISDA_FP_ML_SPECIFICATION
    J = "J"  # OPTION_PRICE_REPORTING_AUTHORITY

class SecurityIDSourceField(FIXFieldBase):
    """"""
    tag: str = "22"
    name: str = "SecurityIDSource"
    type: str = "STRING"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

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
    @property
    def is_h(self) -> bool:
        return self.value == "H"
    @property
    def is_i(self) -> bool:
        return self.value == "I"
    @property
    def is_j(self) -> bool:
        return self.value == "J"
