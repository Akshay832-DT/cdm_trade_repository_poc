"""
FIX MiscFeeBasis field (tag 891).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MiscFeeBasisValues:
    """Enumerated values for MiscFeeBasis."""
    VALUE_0 = "0"  # ABSOLUTE
    VALUE_1 = "1"  # PER_UNIT
    VALUE_2 = "2"  # PERCENTAGE

class MiscFeeBasisField(FIXFieldBase):
    """"""
    tag: str = "891"
    name: str = "MiscFeeBasis"
    type: str = "INT"
    value: Literal["0", "1", "2"]

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
