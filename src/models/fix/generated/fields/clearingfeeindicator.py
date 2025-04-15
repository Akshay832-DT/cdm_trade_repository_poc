"""
FIX ClearingFeeIndicator field (tag 635).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ClearingFeeIndicatorValues:
    """Enumerated values for ClearingFeeIndicator."""
    B = "B"  # CBOE_MEMBER
    C = "C"  # NON_MEMBER_AND_CUSTOMER
    E = "E"  # EQUITY_MEMBER_AND_CLEARING_MEMBER
    F = "F"  # FULL_AND_ASSOCIATE_MEMBER
    H = "H"  # FIRMS106_H_AND106_J
    I = "I"  # GIM
    L = "L"  # LESSEE106_F_EMPLOYEES
    M = "M"  # ALL_OTHER_OWNERSHIP_TYPES
    VALUE_1 = "1"  # FIRST_YEAR_DELEGATE
    VALUE_2 = "2"  # SECOND_YEAR_DELEGATE
    VALUE_3 = "3"  # THIRD_YEAR_DELEGATE
    VALUE_4 = "4"  # FOURTH_YEAR_DELEGATE
    VALUE_5 = "5"  # FIFTH_YEAR_DELEGATE
    VALUE_9 = "9"  # SIXTH_YEAR_DELEGATE

class ClearingFeeIndicatorField(FIXFieldBase):
    """"""
    tag: str = "635"
    name: str = "ClearingFeeIndicator"
    type: str = "STRING"
    value: Literal["B", "C", "E", "F", "H", "I", "L", "M", "1", "2", "3", "4", "5", "9"]

    # Helper methods for enum values
    @property
    def is_b(self) -> bool:
        return self.value == "B"
    @property
    def is_c(self) -> bool:
        return self.value == "C"
    @property
    def is_e(self) -> bool:
        return self.value == "E"
    @property
    def is_f(self) -> bool:
        return self.value == "F"
    @property
    def is_h(self) -> bool:
        return self.value == "H"
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
    def is_value_9(self) -> bool:
        return self.value == "9"
