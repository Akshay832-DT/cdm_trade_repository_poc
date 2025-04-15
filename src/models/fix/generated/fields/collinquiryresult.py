"""
FIX CollInquiryResult field (tag 946).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CollInquiryResultValues:
    """Enumerated values for CollInquiryResult."""
    VALUE_0 = "0"  # SUCCESSFUL
    VALUE_1 = "1"  # INVALID_OR_UNKNOWN_INSTRUMENT
    VALUE_2 = "2"  # INVALID_OR_UNKNOWN_COLLATERAL_TYPE
    VALUE_3 = "3"  # INVALID_PARTIES
    VALUE_4 = "4"  # INVALID_TRANSPORT_TYPE_REQUESTED
    VALUE_5 = "5"  # INVALID_DESTINATION_REQUESTED
    VALUE_6 = "6"  # NO_COLLATERAL_FOUND_FOR_THE_TRADE_SPECIFIED
    VALUE_7 = "7"  # NO_COLLATERAL_FOUND_FOR_THE_ORDER_SPECIFIED
    VALUE_8 = "8"  # COLLATERAL_INQUIRY_TYPE_NOT_SUPPORTED
    VALUE_9 = "9"  # UNAUTHORIZED_FOR_COLLATERAL_INQUIRY
    VALUE_99 = "99"  # OTHER

class CollInquiryResultField(FIXFieldBase):
    """"""
    tag: str = "946"
    name: str = "CollInquiryResult"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "99"]

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
    @property
    def is_value_8(self) -> bool:
        return self.value == "8"
    @property
    def is_value_9(self) -> bool:
        return self.value == "9"
    @property
    def is_value_99(self) -> bool:
        return self.value == "99"
