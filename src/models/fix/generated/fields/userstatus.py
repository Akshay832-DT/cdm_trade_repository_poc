"""
FIX UserStatus field (tag 926).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UserStatusValues:
    """Enumerated values for UserStatus."""
    VALUE_1 = "1"  # LOGGED_IN
    VALUE_2 = "2"  # NOT_LOGGED_IN
    VALUE_3 = "3"  # USER_NOT_RECOGNISED
    VALUE_4 = "4"  # PASSWORD_INCORRECT
    VALUE_5 = "5"  # PASSWORD_CHANGED
    VALUE_6 = "6"  # OTHER

class UserStatusField(FIXFieldBase):
    """"""
    tag: str = "926"
    name: str = "UserStatus"
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
