"""
FIX CollInquiryStatus field (tag 945).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CollInquiryStatusValues:
    """Enumerated values for CollInquiryStatus."""
    VALUE_0 = "0"  # ACCEPTED
    VALUE_1 = "1"  # ACCEPTED_WITH_WARNINGS
    VALUE_2 = "2"  # COMPLETED
    VALUE_3 = "3"  # COMPLETED_WITH_WARNINGS
    VALUE_4 = "4"  # REJECTED

class CollInquiryStatusField(FIXFieldBase):
    """"""
    tag: str = "945"
    name: str = "CollInquiryStatus"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4"]

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
    @property
    def is_value_4(self) -> bool:
        return self.value == "4"
