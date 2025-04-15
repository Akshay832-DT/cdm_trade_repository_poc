"""
FIX PosReqStatus field (tag 729).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PosReqStatusValues:
    """Enumerated values for PosReqStatus."""
    VALUE_0 = "0"  # COMPLETED
    VALUE_1 = "1"  # COMPLETED_WITH_WARNINGS
    VALUE_2 = "2"  # REJECTED

class PosReqStatusField(FIXFieldBase):
    """"""
    tag: str = "729"
    name: str = "PosReqStatus"
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
