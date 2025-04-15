"""
FIX TrdRptStatus field (tag 939).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TrdRptStatusValues:
    """Enumerated values for TrdRptStatus."""
    VALUE_0 = "0"  # ACCEPTED
    VALUE_1 = "1"  # REJECTED

class TrdRptStatusField(FIXFieldBase):
    """"""
    tag: str = "939"
    name: str = "TrdRptStatus"
    type: str = "INT"
    value: Literal["0", "1"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
