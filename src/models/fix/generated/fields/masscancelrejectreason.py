"""
FIX MassCancelRejectReason field (tag 532).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MassCancelRejectReasonValues:
    """Enumerated values for MassCancelRejectReason."""
    VALUE_0 = "0"  # MASS_CANCEL_NOT_SUPPORTED
    VALUE_1 = "1"  # INVALID_OR_UNKNOWN_SECURITY
    VALUE_2 = "2"  # INVALID_OR_UNKOWN_UNDERLYING_SECURITY
    VALUE_3 = "3"  # INVALID_OR_UNKNOWN_PRODUCT
    VALUE_4 = "4"  # INVALID_OR_UNKNOWN_CFI_CODE
    VALUE_5 = "5"  # INVALID_OR_UNKNOWN_SECURITY_TYPE
    VALUE_6 = "6"  # INVALID_OR_UNKNOWN_TRADING_SESSION
    VALUE_99 = "99"  # OTHER

class MassCancelRejectReasonField(FIXFieldBase):
    """"""
    tag: str = "532"
    name: str = "MassCancelRejectReason"
    type: str = "CHAR"
    value: Literal["0", "1", "2", "3", "4", "5", "6", "99"]

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
    @property
    def is_value_4(self) -> bool:
        return self.value == "4"
    @property
    def is_value_5(self) -> bool:
        return self.value == "5"
    @property
    def is_value_6(self) -> bool:
        return self.value == "6"
    @property
    def is_value_99(self) -> bool:
        return self.value == "99"
