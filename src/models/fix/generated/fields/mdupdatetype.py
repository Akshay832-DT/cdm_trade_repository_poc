"""
FIX MDUpdateType field (tag 265).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDUpdateTypeValues:
    """Enumerated values for MDUpdateType."""
    VALUE_0 = "0"  # FULL_REFRESH
    VALUE_1 = "1"  # INCREMENTAL_REFRESH

class MDUpdateTypeField(FIXFieldBase):
    """"""
    tag: str = "265"
    name: str = "MDUpdateType"
    type: str = "INT"
    value: Literal["0", "1"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
