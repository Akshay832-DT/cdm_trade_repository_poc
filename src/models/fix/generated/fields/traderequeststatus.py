"""
FIX TradeRequestStatus field (tag 750).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeRequestStatusValues:
    """Enumerated values for TradeRequestStatus."""
    VALUE_0 = "0"  # ACCEPTED
    VALUE_1 = "1"  # COMPLETED
    VALUE_2 = "2"  # REJECTED

class TradeRequestStatusField(FIXFieldBase):
    """"""
    tag: str = "750"
    name: str = "TradeRequestStatus"
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
