"""
FIX ExpirationCycle field (tag 827).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ExpirationCycleValues:
    """Enumerated values for ExpirationCycle."""
    VALUE_0 = "0"  # EXPIRE_ON_TRADING_SESSION_CLOSE
    VALUE_1 = "1"  # EXPIRE_ON_TRADING_SESSION_OPEN

class ExpirationCycleField(FIXFieldBase):
    """"""
    tag: str = "827"
    name: str = "ExpirationCycle"
    type: str = "INT"
    value: Literal["0", "1"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
