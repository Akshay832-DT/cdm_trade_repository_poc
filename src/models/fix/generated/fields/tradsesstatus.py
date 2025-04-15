"""
FIX TradSesStatus field (tag 340).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradSesStatusValues:
    """Enumerated values for TradSesStatus."""
    VALUE_0 = "0"  # UNKNOWN
    VALUE_1 = "1"  # HALTED
    VALUE_2 = "2"  # OPEN
    VALUE_3 = "3"  # CLOSED
    VALUE_4 = "4"  # PRE_OPEN
    VALUE_5 = "5"  # PRE_CLOSE
    VALUE_6 = "6"  # REQUEST_REJECTED

class TradSesStatusField(FIXFieldBase):
    """"""
    tag: str = "340"
    name: str = "TradSesStatus"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "5", "6"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
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
