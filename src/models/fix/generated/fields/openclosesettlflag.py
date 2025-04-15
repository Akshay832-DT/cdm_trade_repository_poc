"""
FIX OpenCloseSettlFlag field (tag 286).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OpenCloseSettlFlagValues:
    """Enumerated values for OpenCloseSettlFlag."""
    VALUE_0 = "0"  # DAILY_OPEN
    VALUE_1 = "1"  # SESSION_OPEN
    VALUE_2 = "2"  # DELIVERY_SETTLEMENT_ENTRY
    VALUE_3 = "3"  # EXPECTED_ENTRY
    VALUE_4 = "4"  # ENTRY_FROM_PREVIOUS_BUSINESS_DAY
    VALUE_5 = "5"  # THEORETICAL_PRICE_VALUE

class OpenCloseSettlFlagField(FIXFieldBase):
    """"""
    tag: str = "286"
    name: str = "OpenCloseSettlFlag"
    type: str = "MULTIPLEVALUESTRING"
    value: List[str]

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
