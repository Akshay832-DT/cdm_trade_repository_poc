"""
FIX SecurityRequestType field (tag 321).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecurityRequestTypeValues:
    """Enumerated values for SecurityRequestType."""
    VALUE_0 = "0"  # REQUEST_SECURITY_IDENTITY_AND_SPECIFICATIONS
    VALUE_1 = "1"  # REQUEST_SECURITY_IDENTITY_FOR_SPECIFICATIONS
    VALUE_2 = "2"  # REQUEST_LIST_SECURITY_TYPES
    VALUE_3 = "3"  # REQUEST_LIST_SECURITIES

class SecurityRequestTypeField(FIXFieldBase):
    """"""
    tag: str = "321"
    name: str = "SecurityRequestType"
    type: str = "INT"
    value: Literal["0", "1", "2", "3"]

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
