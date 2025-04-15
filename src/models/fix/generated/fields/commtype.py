"""
FIX CommType field (tag 13).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CommTypeValues:
    """Enumerated values for CommType."""
    VALUE_1 = "1"  # PER_UNIT
    VALUE_2 = "2"  # PERCENT
    VALUE_3 = "3"  # ABSOLUTE
    VALUE_4 = "4"  # PERCENTAGE_WAIVED_CASH_DISCOUNT
    VALUE_5 = "5"  # PERCENTAGE_WAIVED_ENHANCED_UNITS
    VALUE_6 = "6"  # POINTS_PER_BOND_OR_CONTRACT

class CommTypeField(FIXFieldBase):
    """"""
    tag: str = "13"
    name: str = "CommType"
    type: str = "CHAR"
    value: Literal["1", "2", "3", "4", "5", "6"]

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
