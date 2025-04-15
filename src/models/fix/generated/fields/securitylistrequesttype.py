"""
FIX SecurityListRequestType field (tag 559).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecurityListRequestTypeValues:
    """Enumerated values for SecurityListRequestType."""
    VALUE_0 = "0"  # SYMBOL
    VALUE_1 = "1"  # SECURITY_TYPE_AND
    VALUE_2 = "2"  # PRODUCT
    VALUE_3 = "3"  # TRADING_SESSION_ID
    VALUE_4 = "4"  # ALL_SECURITIES

class SecurityListRequestTypeField(FIXFieldBase):
    """"""
    tag: str = "559"
    name: str = "SecurityListRequestType"
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
