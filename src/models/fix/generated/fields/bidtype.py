"""
FIX BidType field (tag 394).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BidTypeValues:
    """Enumerated values for BidType."""
    VALUE_1 = "1"  # NON_DISCLOSED
    VALUE_2 = "2"  # DISCLOSED
    VALUE_3 = "3"  # NO_BIDDING_PROCESS

class BidTypeField(FIXFieldBase):
    """"""
    tag: str = "394"
    name: str = "BidType"
    type: str = "INT"
    value: Literal["1", "2", "3"]

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
