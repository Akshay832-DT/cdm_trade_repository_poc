"""
FIX CxlRejResponseTo field (tag 434).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CxlRejResponseToValues:
    """Enumerated values for CxlRejResponseTo."""
    VALUE_1 = "1"  # ORDER_CANCEL_REQUEST
    VALUE_2 = "2"  # ORDER_CANCEL

class CxlRejResponseToField(FIXFieldBase):
    """"""
    tag: str = "434"
    name: str = "CxlRejResponseTo"
    type: str = "CHAR"
    value: Literal["1", "2"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
