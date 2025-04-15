"""
FIX AdjustmentType field (tag 718).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AdjustmentTypeValues:
    """Enumerated values for AdjustmentType."""
    VALUE_0 = "0"  # PROCESS_REQUEST_AS_MARGIN_DISPOSITION
    VALUE_1 = "1"  # DELTA_PLUS
    VALUE_2 = "2"  # DELTA_MINUS
    VALUE_3 = "3"  # FINAL

class AdjustmentTypeField(FIXFieldBase):
    """"""
    tag: str = "718"
    name: str = "AdjustmentType"
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
