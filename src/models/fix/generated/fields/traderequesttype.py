"""
FIX TradeRequestType field (tag 569).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeRequestTypeValues:
    """Enumerated values for TradeRequestType."""
    VALUE_0 = "0"  # ALL_TRADES
    VALUE_1 = "1"  # MATCHED_TRADES_MATCHING_CRITERIA
    VALUE_2 = "2"  # UNMATCHED_TRADES_THAT_MATCH_CRITERIA
    VALUE_3 = "3"  # UNREPORTED_TRADES_THAT_MATCH_CRITERIA
    VALUE_4 = "4"  # ADVISORIES_THAT_MATCH_CRITERIA

class TradeRequestTypeField(FIXFieldBase):
    """"""
    tag: str = "569"
    name: str = "TradeRequestType"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4"]

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
