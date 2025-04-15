"""
FIX QuoteCancelType field (tag 298).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteCancelTypeValues:
    """Enumerated values for QuoteCancelType."""
    VALUE_1 = "1"  # CANCEL_FOR_ONE_OR_MORE_SECURITIES
    VALUE_2 = "2"  # CANCEL_FOR_SECURITY_TYPE
    VALUE_3 = "3"  # CANCEL_FOR_UNDERLYING_SECURITY
    VALUE_4 = "4"  # CANCEL_ALL_QUOTES

class QuoteCancelTypeField(FIXFieldBase):
    """"""
    tag: str = "298"
    name: str = "QuoteCancelType"
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
