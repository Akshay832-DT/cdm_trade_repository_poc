"""
FIX ExecRestatementReason field (tag 378).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ExecRestatementReasonValues:
    """Enumerated values for ExecRestatementReason."""
    VALUE_0 = "0"  # GT_CORPORATE_ACTION
    VALUE_1 = "1"  # GT_RENEWAL
    VALUE_2 = "2"  # VERBAL_CHANGE
    VALUE_3 = "3"  # REPRICING_OF_ORDER
    VALUE_4 = "4"  # BROKER_OPTION
    VALUE_5 = "5"  # PARTIAL_DECLINE_OF_ORDER_QTY
    VALUE_6 = "6"  # CANCEL_ON_TRADING_HALT
    VALUE_7 = "7"  # CANCEL_ON_SYSTEM_FAILURE
    VALUE_8 = "8"  # MARKET
    VALUE_9 = "9"  # CANCELED
    VALUE_10 = "10"  # WAREHOUSE_RECAP
    VALUE_99 = "99"  # OTHER

class ExecRestatementReasonField(FIXFieldBase):
    """"""
    tag: str = "378"
    name: str = "ExecRestatementReason"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "99"]

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
    def is_value_10(self) -> bool:
        return self.value == "10"
    @property
    def is_value_99(self) -> bool:
        return self.value == "99"
