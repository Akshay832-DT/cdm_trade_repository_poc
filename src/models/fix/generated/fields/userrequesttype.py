"""
FIX UserRequestType field (tag 924).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UserRequestTypeValues:
    """Enumerated values for UserRequestType."""
    VALUE_1 = "1"  # LOG_ON_USER
    VALUE_2 = "2"  # LOG_OFF_USER
    VALUE_3 = "3"  # CHANGE_PASSWORD_FOR_USER
    VALUE_4 = "4"  # REQUEST_INDIVIDUAL_USER_STATUS

class UserRequestTypeField(FIXFieldBase):
    """"""
    tag: str = "924"
    name: str = "UserRequestType"
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
