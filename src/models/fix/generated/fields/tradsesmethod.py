"""
FIX TradSesMethod field (tag 338).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradSesMethodValues:
    """Enumerated values for TradSesMethod."""
    VALUE_1 = "1"  # ELECTRONIC
    VALUE_2 = "2"  # OPEN_OUTCRY
    VALUE_3 = "3"  # TWO_PARTY

class TradSesMethodField(FIXFieldBase):
    """"""
    tag: str = "338"
    name: str = "TradSesMethod"
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
