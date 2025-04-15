"""
FIX TradSesMode field (tag 339).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradSesModeValues:
    """Enumerated values for TradSesMode."""
    VALUE_1 = "1"  # TESTING
    VALUE_2 = "2"  # SIMULATED
    VALUE_3 = "3"  # PRODUCTION

class TradSesModeField(FIXFieldBase):
    """"""
    tag: str = "339"
    name: str = "TradSesMode"
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
