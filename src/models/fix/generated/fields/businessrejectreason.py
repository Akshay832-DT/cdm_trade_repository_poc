"""
FIX BusinessRejectReason field (tag 380).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BusinessRejectReasonValues:
    """Enumerated values for BusinessRejectReason."""
    VALUE_0 = "0"  # OTHER
    VALUE_1 = "1"  # UNKNOWN_ID
    VALUE_2 = "2"  # UNKNOWN_SECURITY
    VALUE_3 = "3"  # UNSUPPORTED_MESSAGE_TYPE
    VALUE_4 = "4"  # APPLICATION_NOT_AVAILABLE
    VALUE_5 = "5"  # CONDITIONALLY_REQUIRED_FIELD_MISSING
    VALUE_6 = "6"  # NOT_AUTHORIZED
    VALUE_7 = "7"  # DELIVER_TO_FIRM_NOT_AVAILABLE_AT_THIS_TIME

class BusinessRejectReasonField(FIXFieldBase):
    """"""
    tag: str = "380"
    name: str = "BusinessRejectReason"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "5", "6", "7"]

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
    def is_value_7(self) -> bool:
        return self.value == "7"
