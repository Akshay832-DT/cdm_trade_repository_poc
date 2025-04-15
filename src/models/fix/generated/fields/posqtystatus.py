"""
FIX PosQtyStatus field (tag 706).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PosQtyStatusValues:
    """Enumerated values for PosQtyStatus."""
    VALUE_0 = "0"  # SUBMITTED
    VALUE_1 = "1"  # ACCEPTED
    VALUE_2 = "2"  # REJECTED

class PosQtyStatusField(FIXFieldBase):
    """"""
    tag: str = "706"
    name: str = "PosQtyStatus"
    type: str = "INT"
    value: Literal["0", "1", "2"]

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
