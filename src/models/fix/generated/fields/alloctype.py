"""
FIX AllocType field (tag 626).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocTypeValues:
    """Enumerated values for AllocType."""
    VALUE_1 = "1"  # CALCULATED
    VALUE_2 = "2"  # PRELIMINARY
    VALUE_5 = "5"  # READY_TO_BOOK
    VALUE_7 = "7"  # WAREHOUSE_INSTRUCTION
    VALUE_8 = "8"  # REQUEST_TO_INTERMEDIARY

class AllocTypeField(FIXFieldBase):
    """"""
    tag: str = "626"
    name: str = "AllocType"
    type: str = "INT"
    value: Literal["1", "2", "5", "7", "8"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
    @property
    def is_value_5(self) -> bool:
        return self.value == "5"
    @property
    def is_value_7(self) -> bool:
        return self.value == "7"
    @property
    def is_value_8(self) -> bool:
        return self.value == "8"
