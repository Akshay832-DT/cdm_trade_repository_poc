"""
FIX AllocIntermedReqType field (tag 808).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocIntermedReqTypeValues:
    """Enumerated values for AllocIntermedReqType."""
    VALUE_1 = "1"  # PENDING_ACCEPT
    VALUE_2 = "2"  # PENDING_RELEASE
    VALUE_3 = "3"  # PENDING_REVERSAL
    VALUE_4 = "4"  # ACCEPT
    VALUE_5 = "5"  # BLOCK_LEVEL_REJECT
    VALUE_6 = "6"  # ACCOUNT_LEVEL_REJECT

class AllocIntermedReqTypeField(FIXFieldBase):
    """"""
    tag: str = "808"
    name: str = "AllocIntermedReqType"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6"]

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
    @property
    def is_value_6(self) -> bool:
        return self.value == "6"
