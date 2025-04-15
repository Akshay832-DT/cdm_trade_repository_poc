"""
FIX PreallocMethod field (tag 591).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PreallocMethodValues:
    """Enumerated values for PreallocMethod."""
    VALUE_0 = "0"  # PRO_RATA
    VALUE_1 = "1"  # DO_NOT_PRO_RATA

class PreallocMethodField(FIXFieldBase):
    """"""
    tag: str = "591"
    name: str = "PreallocMethod"
    type: str = "CHAR"
    value: Literal["0", "1"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
