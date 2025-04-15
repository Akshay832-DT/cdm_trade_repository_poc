"""
FIX SecurityTradingStatus field (tag 326).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecurityTradingStatusValues:
    """Enumerated values for SecurityTradingStatus."""
    VALUE_1 = "1"  # OPENING_DELAY
    VALUE_2 = "2"  # TRADING_HALT
    VALUE_3 = "3"  # RESUME
    VALUE_4 = "4"  # NO_OPEN
    VALUE_5 = "5"  # PRICE_INDICATION
    VALUE_6 = "6"  # TRADING_RANGE_INDICATION
    VALUE_7 = "7"  # MARKET_IMBALANCE_BUY
    VALUE_8 = "8"  # MARKET_IMBALANCE_SELL
    VALUE_9 = "9"  # MARKET_ON_CLOSE_IMBALANCE_BUY
    VALUE_10 = "10"  # MARKET_ON_CLOSE_IMBALANCE_SELL
    VALUE_12 = "12"  # NO_MARKET_IMBALANCE
    VALUE_13 = "13"  # NO_MARKET_ON_CLOSE_IMBALANCE
    VALUE_14 = "14"  # ITS_PRE_OPENING
    VALUE_15 = "15"  # NEW_PRICE_INDICATION
    VALUE_16 = "16"  # TRADE_DISSEMINATION_TIME
    VALUE_17 = "17"  # READY_TO_TRADE
    VALUE_18 = "18"  # NOT_AVAILABLE_FOR_TRADING
    VALUE_19 = "19"  # NOT_TRADED_ON_THIS_MARKET
    VALUE_20 = "20"  # UNKNOWN_OR_INVALID
    VALUE_21 = "21"  # PRE_OPEN
    VALUE_22 = "22"  # OPENING_ROTATION
    VALUE_23 = "23"  # FAST_MARKET

class SecurityTradingStatusField(FIXFieldBase):
    """"""
    tag: str = "326"
    name: str = "SecurityTradingStatus"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]

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
    @property
    def is_value_16(self) -> bool:
        return self.value == "16"
    @property
    def is_value_17(self) -> bool:
        return self.value == "17"
    @property
    def is_value_18(self) -> bool:
        return self.value == "18"
    @property
    def is_value_19(self) -> bool:
        return self.value == "19"
    @property
    def is_value_20(self) -> bool:
        return self.value == "20"
    @property
    def is_value_21(self) -> bool:
        return self.value == "21"
    @property
    def is_value_22(self) -> bool:
        return self.value == "22"
    @property
    def is_value_23(self) -> bool:
        return self.value == "23"
