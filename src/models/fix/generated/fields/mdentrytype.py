"""
FIX MDEntryType field (tag 269).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDEntryTypeValues:
    """Enumerated values for MDEntryType."""
    VALUE_0 = "0"  # BID
    VALUE_1 = "1"  # OFFER
    VALUE_2 = "2"  # TRADE
    VALUE_3 = "3"  # INDEX_VALUE
    VALUE_4 = "4"  # OPENING_PRICE
    VALUE_5 = "5"  # CLOSING_PRICE
    VALUE_6 = "6"  # SETTLEMENT_PRICE
    VALUE_7 = "7"  # TRADING_SESSION_HIGH_PRICE
    VALUE_8 = "8"  # TRADING_SESSION_LOW_PRICE
    VALUE_9 = "9"  # TRADING_SESSION_VWAP_PRICE
    A = "A"  # IMBALANCE
    B = "B"  # TRADE_VOLUME
    C = "C"  # OPEN_INTEREST

class MDEntryTypeField(FIXFieldBase):
    """"""
    tag: str = "269"
    name: str = "MDEntryType"
    type: str = "CHAR"
    value: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C"]

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
    def is_a(self) -> bool:
        return self.value == "A"
    @property
    def is_b(self) -> bool:
        return self.value == "B"
    @property
    def is_c(self) -> bool:
        return self.value == "C"
