"""
FIX BookingUnit field (tag 590).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BookingUnitValues:
    """Enumerated values for BookingUnit."""
    VALUE_0 = "0"  # EACH_PARTIAL_EXECUTION_IS_A_BOOKABLE_UNIT
    VALUE_1 = "1"  # AGGREGATE_PARTIAL_EXECUTIONS_ON_THIS_ORDER
    VALUE_2 = "2"  # AGGREGATE_EXECUTIONS_FOR_THIS_SYMBOL

class BookingUnitField(FIXFieldBase):
    """"""
    tag: str = "590"
    name: str = "BookingUnit"
    type: str = "CHAR"
    value: Literal["0", "1", "2"]

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
