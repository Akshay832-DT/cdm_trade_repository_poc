"""
FIX PaymentMethod field (tag 492).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PaymentMethodValues:
    """Enumerated values for PaymentMethod."""
    VALUE_1 = "1"  # CREST
    VALUE_2 = "2"  # NSCC
    VALUE_3 = "3"  # EUROCLEAR
    VALUE_4 = "4"  # CLEARSTREAM
    VALUE_5 = "5"  # CHEQUE
    VALUE_6 = "6"  # TELEGRAPHIC_TRANSFER
    VALUE_7 = "7"  # FED_WIRE
    VALUE_8 = "8"  # DEBIT_CARD
    VALUE_9 = "9"  # DIRECT_DEBIT
    VALUE_10 = "10"  # DIRECT_CREDIT
    VALUE_11 = "11"  # CREDIT_CARD
    VALUE_12 = "12"  # ACH_DEBIT
    VALUE_13 = "13"  # ACH_CREDIT
    VALUE_14 = "14"  # BPAY
    VALUE_15 = "15"  # HIGH_VALUE_CLEARING_SYSTEM

class PaymentMethodField(FIXFieldBase):
    """"""
    tag: str = "492"
    name: str = "PaymentMethod"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]

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
    @property
    def is_value_13(self) -> bool:
        return self.value == "13"
    @property
    def is_value_14(self) -> bool:
        return self.value == "14"
    @property
    def is_value_15(self) -> bool:
        return self.value == "15"
