"""
FIX TradeReportRejectReason field (tag 751).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeReportRejectReasonValues:
    """Enumerated values for TradeReportRejectReason."""
    VALUE_0 = "0"  # SUCCESSFUL
    VALUE_1 = "1"  # INVALID_PARTY_ONFORMATION
    VALUE_2 = "2"  # UNKNOWN_INSTRUMENT
    VALUE_3 = "3"  # UNAUTHORIZED_TO_REPORT_TRADES
    VALUE_4 = "4"  # INVALID_TRADE_TYPE
    VALUE_99 = "99"  # OTHER

class TradeReportRejectReasonField(FIXFieldBase):
    """"""
    tag: str = "751"
    name: str = "TradeReportRejectReason"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "99"]

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
    def is_value_99(self) -> bool:
        return self.value == "99"
