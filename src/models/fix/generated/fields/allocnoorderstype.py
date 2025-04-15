"""
FIX AllocNoOrdersType field (tag 857).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocNoOrdersTypeValues:
    """Enumerated values for AllocNoOrdersType."""
    VALUE_0 = "0"  # NOT_SPECIFIED
    VALUE_1 = "1"  # EXPLICIT_LIST_PROVIDED

class AllocNoOrdersTypeField(FIXFieldBase):
    """"""
    tag: str = "857"
    name: str = "AllocNoOrdersType"
    type: str = "INT"
    value: Literal["0", "1"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
