"""
FIX AffirmStatus field (tag 940).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AffirmStatusValues:
    """Enumerated values for AffirmStatus."""
    VALUE_1 = "1"  # RECEIVED
    VALUE_2 = "2"  # CONFIRM_REJECTED
    VALUE_3 = "3"  # AFFIRMED

class AffirmStatusField(FIXFieldBase):
    """"""
    tag: str = "940"
    name: str = "AffirmStatus"
    type: str = "INT"
    value: Literal["1", "2", "3"]

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
