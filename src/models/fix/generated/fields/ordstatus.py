"""
FIX OrdStatus field (tag 39).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrdStatusValues:
    """Enumerated values for OrdStatus."""
    VALUE_0 = "0"  # NEW
    VALUE_1 = "1"  # PARTIALLY_FILLED
    VALUE_2 = "2"  # FILLED
    VALUE_3 = "3"  # DONE_FOR_DAY
    VALUE_4 = "4"  # CANCELED
    VALUE_6 = "6"  # PENDING_CANCEL
    VALUE_7 = "7"  # STOPPED
    VALUE_8 = "8"  # REJECTED
    VALUE_9 = "9"  # SUSPENDED
    A = "A"  # PENDING_NEW
    B = "B"  # CALCULATED
    C = "C"  # EXPIRED
    D = "D"  # ACCEPTED_FOR_BIDDING
    E = "E"  # PENDING_REPLACE

class OrdStatusField(FIXFieldBase):
    """"""
    tag: str = "39"
    name: str = "OrdStatus"
    type: str = "CHAR"
    value: Literal["0", "1", "2", "3", "4", "6", "7", "8", "9", "A", "B", "C", "D", "E"]

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
    def is_a(self) -> bool:
        return self.value == "A"
    @property
    def is_b(self) -> bool:
        return self.value == "B"
    @property
    def is_c(self) -> bool:
        return self.value == "C"
    @property
    def is_d(self) -> bool:
        return self.value == "D"
    @property
    def is_e(self) -> bool:
        return self.value == "E"
