"""
FIX StatusValue field (tag 928).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class StatusValueValues:
    """Enumerated values for StatusValue."""
    VALUE_1 = "1"  # CONNECTED
    VALUE_2 = "2"  # NOT_CONNECTED_UNEXPECTED
    VALUE_3 = "3"  # NOT_CONNECTED_EXPECTED
    VALUE_4 = "4"  # IN_PROCESS

class StatusValueField(FIXFieldBase):
    """"""
    tag: str = "928"
    name: str = "StatusValue"
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
