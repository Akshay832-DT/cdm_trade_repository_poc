"""
FIX TradeRequestResult field (tag 749).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeRequestResultValues:
    """Enumerated values for TradeRequestResult."""
    VALUE_0 = "0"  # SUCCESSFUL
    VALUE_1 = "1"  # INVALID_OR_UNKNOWN_INSTRUMENT
    VALUE_2 = "2"  # INVALID_TYPE_OF_TRADE_REQUESTED
    VALUE_3 = "3"  # INVALID_PARTIES
    VALUE_4 = "4"  # INVALID_TRANSPORT_TYPE_REQUESTED
    VALUE_5 = "5"  # INVALID_DESTINATION_REQUESTED
    VALUE_8 = "8"  # TRADE_REQUEST_TYPE_NOT_SUPPORTED
    VALUE_9 = "9"  # NOT_AUTHORIZED
    VALUE_99 = "99"  # OTHER

class TradeRequestResultField(FIXFieldBase):
    """"""
    tag: str = "749"
    name: str = "TradeRequestResult"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "5", "8", "9", "99"]

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
    def is_value_8(self) -> bool:
        return self.value == "8"
    @property
    def is_value_9(self) -> bool:
        return self.value == "9"
    @property
    def is_value_99(self) -> bool:
        return self.value == "99"
