"""
FIX Product field (tag 460).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ProductValues:
    """Enumerated values for Product."""
    VALUE_1 = "1"  # AGENCY
    VALUE_2 = "2"  # COMMODITY
    VALUE_3 = "3"  # CORPORATE
    VALUE_4 = "4"  # CURRENCY
    VALUE_5 = "5"  # EQUITY
    VALUE_6 = "6"  # GOVERNMENT
    VALUE_7 = "7"  # INDEX
    VALUE_8 = "8"  # LOAN
    VALUE_9 = "9"  # MONEYMARKET
    VALUE_10 = "10"  # MORTGAGE
    VALUE_11 = "11"  # MUNICIPAL
    VALUE_12 = "12"  # OTHER
    VALUE_13 = "13"  # FINANCING

class ProductField(FIXFieldBase):
    """"""
    tag: str = "460"
    name: str = "Product"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

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
    def is_value_10(self) -> bool:
        return self.value == "10"
    @property
    def is_value_11(self) -> bool:
        return self.value == "11"
    @property
    def is_value_12(self) -> bool:
        return self.value == "12"
    @property
    def is_value_13(self) -> bool:
        return self.value == "13"
