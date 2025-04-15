"""
FIX OrderRestrictions field (tag 529).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrderRestrictionsValues:
    """Enumerated values for OrderRestrictions."""
    VALUE_1 = "1"  # PROGRAM_TRADE
    VALUE_2 = "2"  # INDEX_ARBITRAGE
    VALUE_3 = "3"  # NON_INDEX_ARBITRAGE
    VALUE_4 = "4"  # COMPETING_MARKET_MAKER
    VALUE_5 = "5"  # ACTING_AS_MARKET_MAKER_OR_SPECIALIST_IN_SECURITY
    VALUE_6 = "6"  # ACTING_AS_MARKET_MAKER_OR_SPECIALIST_IN_UNDERLYING
    VALUE_7 = "7"  # FOREIGN_ENTITY
    VALUE_8 = "8"  # EXTERNAL_MARKET_PARTICIPANT
    VALUE_9 = "9"  # EXTERNAL_INTER_CONNECTED_MARKET_LINKAGE
    A = "A"  # RISKLESS_ARBITRAGE

class OrderRestrictionsField(FIXFieldBase):
    """"""
    tag: str = "529"
    name: str = "OrderRestrictions"
    type: str = "MULTIPLEVALUESTRING"
    value: List[str]

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
    def is_a(self) -> bool:
        return self.value == "A"
