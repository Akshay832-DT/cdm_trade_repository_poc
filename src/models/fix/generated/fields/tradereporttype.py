"""
FIX TradeReportType field (tag 856).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeReportTypeValues:
    """Enumerated values for TradeReportType."""
    VALUE_0 = "0"  # SUBMIT
    VALUE_1 = "1"  # ALLEGED
    VALUE_2 = "2"  # ACCEPT
    VALUE_3 = "3"  # DECLINE
    VALUE_4 = "4"  # ADDENDUM
    VALUE_5 = "5"  # NO
    VALUE_6 = "6"  # TRADE_REPORT_CANCEL
    VALUE_7 = "7"  # LOCKED_IN

class TradeReportTypeField(FIXFieldBase):
    """"""
    tag: str = "856"
    name: str = "TradeReportType"
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
