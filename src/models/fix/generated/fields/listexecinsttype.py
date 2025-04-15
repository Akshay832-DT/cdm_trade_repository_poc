"""
FIX ListExecInstType field (tag 433).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ListExecInstTypeValues:
    """Enumerated values for ListExecInstType."""
    VALUE_1 = "1"  # IMMEDIATE
    VALUE_2 = "2"  # WAIT_FOR_INSTRUCTION
    VALUE_3 = "3"  # SELL_DRIVEN
    VALUE_4 = "4"  # BUY_DRIVEN_CASH_TOP_UP
    VALUE_5 = "5"  # BUY_DRIVEN_CASH_WITHDRAW

class ListExecInstTypeField(FIXFieldBase):
    """"""
    tag: str = "433"
    name: str = "ListExecInstType"
    type: str = "CHAR"
    value: Literal["1", "2", "3", "4", "5"]

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
