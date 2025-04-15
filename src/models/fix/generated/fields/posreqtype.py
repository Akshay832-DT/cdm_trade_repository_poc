"""
FIX PosReqType field (tag 724).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PosReqTypeValues:
    """Enumerated values for PosReqType."""
    VALUE_0 = "0"  # POSITIONS
    VALUE_1 = "1"  # TRADES
    VALUE_2 = "2"  # EXERCISES
    VALUE_3 = "3"  # ASSIGNMENTS

class PosReqTypeField(FIXFieldBase):
    """"""
    tag: str = "724"
    name: str = "PosReqType"
    type: str = "INT"
    value: Literal["0", "1", "2", "3"]

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
