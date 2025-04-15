"""
FIX LastCapacity field (tag 29).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LastCapacityValues:
    """Enumerated values for LastCapacity."""
    VALUE_1 = "1"  # AGENT
    VALUE_2 = "2"  # CROSS_AS_AGENT
    VALUE_3 = "3"  # CROSS_AS_PRINCIPAL
    VALUE_4 = "4"  # PRINCIPAL

class LastCapacityField(FIXFieldBase):
    """"""
    tag: str = "29"
    name: str = "LastCapacity"
    type: str = "CHAR"
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
