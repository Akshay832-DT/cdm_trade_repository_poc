"""
FIX ListStatusType field (tag 429).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ListStatusTypeValues:
    """Enumerated values for ListStatusType."""
    VALUE_1 = "1"  # ACK
    VALUE_2 = "2"  # RESPONSE
    VALUE_3 = "3"  # TIMED
    VALUE_4 = "4"  # EXEC_STARTED
    VALUE_5 = "5"  # ALL_DONE
    VALUE_6 = "6"  # ALERT

class ListStatusTypeField(FIXFieldBase):
    """"""
    tag: str = "429"
    name: str = "ListStatusType"
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
