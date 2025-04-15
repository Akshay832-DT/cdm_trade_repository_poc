"""
FIX DistribPaymentMethod field (tag 477).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DistribPaymentMethodValues:
    """Enumerated values for DistribPaymentMethod."""
    VALUE_1 = "1"  # CREST
    VALUE_2 = "2"  # NSCC
    VALUE_3 = "3"  # EUROCLEAR
    VALUE_4 = "4"  # CLEARSTREAM
    VALUE_5 = "5"  # CHEQUE
    VALUE_6 = "6"  # TELEGRAPHIC_TRANSFER
    VALUE_7 = "7"  # FED_WIRE
    VALUE_8 = "8"  # DIRECT_CREDIT
    VALUE_9 = "9"  # ACH_CREDIT
    VALUE_10 = "10"  # BPAY
    VALUE_11 = "11"  # HIGH_VALUE_CLEARING_SYSTEM_HVACS
    VALUE_12 = "12"  # REINVEST_IN_FUND

class DistribPaymentMethodField(FIXFieldBase):
    """"""
    tag: str = "477"
    name: str = "DistribPaymentMethod"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

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
    def is_value_10(self) -> bool:
        return self.value == "10"
    @property
    def is_value_11(self) -> bool:
        return self.value == "11"
    @property
    def is_value_12(self) -> bool:
        return self.value == "12"
