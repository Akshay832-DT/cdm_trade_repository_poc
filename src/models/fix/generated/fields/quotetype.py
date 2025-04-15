"""
FIX QuoteType field (tag 537).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteTypeValues:
    """Enumerated values for QuoteType."""
    VALUE_0 = "0"  # INDICATIVE
    VALUE_1 = "1"  # TRADEABLE
    VALUE_2 = "2"  # RESTRICTED_TRADEABLE
    VALUE_3 = "3"  # COUNTER

class QuoteTypeField(FIXFieldBase):
    """"""
    tag: str = "537"
    name: str = "QuoteType"
    type: str = "INT"
    value: Literal["0", "1", "2", "3"]

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
