"""
FIX SettlInstSource field (tag 165).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlInstSourceValues:
    """Enumerated values for SettlInstSource."""
    VALUE_1 = "1"  # BROKER_CREDIT
    VALUE_2 = "2"  # INSTITUTION
    VALUE_3 = "3"  # INVESTOR

class SettlInstSourceField(FIXFieldBase):
    """"""
    tag: str = "165"
    name: str = "SettlInstSource"
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
