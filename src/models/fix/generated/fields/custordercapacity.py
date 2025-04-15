"""
FIX CustOrderCapacity field (tag 582).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CustOrderCapacityValues:
    """Enumerated values for CustOrderCapacity."""
    VALUE_1 = "1"  # MEMBER_TRADING_FOR_THEIR_OWN_ACCOUNT
    VALUE_2 = "2"  # CLEARING_FIRM_TRADING_FOR_ITS_PROPRIETARY_ACCOUNT
    VALUE_3 = "3"  # MEMBER_TRADING_FOR_ANOTHER_MEMBER
    VALUE_4 = "4"  # ALL_OTHER

class CustOrderCapacityField(FIXFieldBase):
    """"""
    tag: str = "582"
    name: str = "CustOrderCapacity"
    type: str = "INT"
    value: Literal["1", "2", "3", "4"]

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
