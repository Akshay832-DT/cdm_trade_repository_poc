"""
FIX CxlRejReason field (tag 102).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CxlRejReasonValues:
    """Enumerated values for CxlRejReason."""
    VALUE_0 = "0"  # TOO_LATE_TO_CANCEL
    VALUE_1 = "1"  # UNKNOWN_ORDER
    VALUE_2 = "2"  # BROKER_CREDIT
    VALUE_3 = "3"  # ORDER_ALREADY_IN_PENDING_STATUS
    VALUE_4 = "4"  # UNABLE_TO_PROCESS_ORDER_MASS_CANCEL_REQUEST
    VALUE_5 = "5"  # ORIG_ORD_MOD_TIME
    VALUE_6 = "6"  # DUPLICATE_CL_ORD_ID
    VALUE_99 = "99"  # OTHER

class CxlRejReasonField(FIXFieldBase):
    """"""
    tag: str = "102"
    name: str = "CxlRejReason"
    type: str = "INT"
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
