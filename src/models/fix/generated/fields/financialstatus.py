"""
FIX FinancialStatus field (tag 291).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class FinancialStatusValues:
    """Enumerated values for FinancialStatus."""
    VALUE_1 = "1"  # BANKRUPT
    VALUE_2 = "2"  # PENDING_DELISTING

class FinancialStatusField(FIXFieldBase):
    """"""
    tag: str = "291"
    name: str = "FinancialStatus"
    type: str = "MULTIPLEVALUESTRING"
    value: List[str]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
