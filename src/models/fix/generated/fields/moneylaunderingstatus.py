"""
FIX MoneyLaunderingStatus field (tag 481).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MoneyLaunderingStatusValues:
    """Enumerated values for MoneyLaunderingStatus."""
    Y = "Y"  # PASSED
    N = "N"  # NOT_CHECKED
    VALUE_1 = "1"  # EXEMPT_BELOW_LIMIT
    VALUE_2 = "2"  # EXEMPT_MONEY_TYPE
    VALUE_3 = "3"  # EXEMPT_AUTHORISED

class MoneyLaunderingStatusField(FIXFieldBase):
    """"""
    tag: str = "481"
    name: str = "MoneyLaunderingStatus"
    type: str = "CHAR"
    value: Literal["Y", "N", "1", "2", "3"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
    @property
    def is_value_3(self) -> bool:
        return self.value == "3"
