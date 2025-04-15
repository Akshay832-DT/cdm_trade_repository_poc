"""
FIX TradSesStatusRejReason field (tag 567).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradSesStatusRejReasonValues:
    """Enumerated values for TradSesStatusRejReason."""
    VALUE_1 = "1"  # UNKNOWN_OR_INVALID_TRADING_SESSION_ID
    VALUE_99 = "99"  # OTHER

class TradSesStatusRejReasonField(FIXFieldBase):
    """"""
    tag: str = "567"
    name: str = "TradSesStatusRejReason"
    type: str = "INT"
    value: Literal["1", "99"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_99(self) -> bool:
        return self.value == "99"
