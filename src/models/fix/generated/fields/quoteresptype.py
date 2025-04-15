"""
FIX QuoteRespType field (tag 694).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteRespTypeValues:
    """Enumerated values for QuoteRespType."""
    VALUE_1 = "1"  # HIT
    VALUE_2 = "2"  # COUNTER
    VALUE_3 = "3"  # EXPIRED
    VALUE_4 = "4"  # COVER
    VALUE_5 = "5"  # DONE_AWAY
    VALUE_6 = "6"  # PASS

class QuoteRespTypeField(FIXFieldBase):
    """"""
    tag: str = "694"
    name: str = "QuoteRespType"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6"]

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
