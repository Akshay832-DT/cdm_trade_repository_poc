"""
FIX CashMargin field (tag 544).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CashMarginValues:
    """Enumerated values for CashMargin."""
    VALUE_1 = "1"  # CASH
    VALUE_2 = "2"  # MARGIN_OPEN
    VALUE_3 = "3"  # MARGIN_CLOSE

class CashMarginField(FIXFieldBase):
    """"""
    tag: str = "544"
    name: str = "CashMargin"
    type: str = "CHAR"
    value: Literal["1", "2", "3"]

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
