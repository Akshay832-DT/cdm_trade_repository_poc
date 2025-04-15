"""
FIX ListOrderStatus field (tag 431).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ListOrderStatusValues:
    """Enumerated values for ListOrderStatus."""
    VALUE_1 = "1"  # IN_BIDDING_PROCESS
    VALUE_2 = "2"  # RECEIVED_FOR_EXECUTION
    VALUE_3 = "3"  # EXECUTING
    VALUE_4 = "4"  # CANCELLING
    VALUE_5 = "5"  # ALERT
    VALUE_6 = "6"  # ALL_DONE
    VALUE_7 = "7"  # REJECT

class ListOrderStatusField(FIXFieldBase):
    """"""
    tag: str = "431"
    name: str = "ListOrderStatus"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6", "7"]

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
    @property
    def is_value_7(self) -> bool:
        return self.value == "7"
