"""
FIX TrdRegTimestampType field (tag 770).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TrdRegTimestampTypeValues:
    """Enumerated values for TrdRegTimestampType."""
    VALUE_1 = "1"  # EXECUTION_TIME
    VALUE_2 = "2"  # TIME_IN
    VALUE_3 = "3"  # TIME_OUT
    VALUE_4 = "4"  # BROKER_RECEIPT
    VALUE_5 = "5"  # BROKER_EXECUTION

class TrdRegTimestampTypeField(FIXFieldBase):
    """"""
    tag: str = "770"
    name: str = "TrdRegTimestampType"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5"]

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
